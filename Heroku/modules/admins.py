from asyncio import QueueEmpty

from pytgcalls.types.input_stream import InputAudioStream
from pytgcalls.types.input_stream import InputStream

from pyrogram import Client, filters
from pyrogram.types import Message

from Heroku.config import que
from Heroku.core.queue import (
    is_active_chat,
    add_active_chat,
    remove_active_chat,
    music_on,
    is_music_playing,
    music_off,
)
from Heroku.calls import calls
from Heroku.setup.filters import command, other_filters
from Heroku.setup.decorators import sudo_users_only
from Heroku.calls.queues import clear, get, is_empty, put, task_done


async def member_permissions(chat_id: int, user_id: int):
    perms = []
    try:
        member = await app.get_chat_member(chat_id, user_id)
    except Exception:
        return []
    if member.can_post_messages:
        perms.append("can_post_messages")
    if member.can_edit_messages:
        perms.append("can_edit_messages")
    if member.can_delete_messages:
        perms.append("can_delete_messages")
    if member.can_restrict_members:
        perms.append("can_restrict_members")
    if member.can_promote_members:
        perms.append("can_promote_members")
    if member.can_change_info:
        perms.append("can_change_info")
    if member.can_invite_users:
        perms.append("can_invite_users")
    if member.can_pin_messages:
        perms.append("can_pin_messages")
    if member.can_manage_voice_chats:
        perms.append("can_manage_voice_chats")
    return perms


from Heroku.setup.administrator import adminsOnly


@Client.on_message(command(["durdur"]) & other_filters)
async def pause(app: Client, message: Message):
    if message.sender_chat:
        return await message.reply_text(
            "🔴 __Siz bir **Anonim Yöneticisiniz**!__\n│\n╰ Yönetici haklarından kullanıcı hesabına geri dön."
        )
    permission = "can_delete_messages"
    m = await adminsOnly(permission, message)
    if m == 1:
        return
    checking = message.from_user.mention
    chat_id = message.chat.id
    if not await is_active_chat(chat_id):
        return await message.reply_text(
            "• Bot sesli sohbette yayın yapmıyor."
        )
    elif not await is_music_playing(message.chat.id):
        return await message.reply_text(
            "• Bot sesli sohbette yayın yapmıyor."
        )
    await music_off(chat_id)
    await calls.pytgcalls.pause_stream(chat_id)
    await message.reply_text(
        f"• Durduran : {checking}"
    )


@Client.on_message(command(["devam"]) & other_filters)
async def resume(app: Client, message: Message):
    if message.sender_chat:
        return await message.reply_text(
            "🔴 __Siz bir **Anonim Yöneticisiniz**!__\n│\n╰ Yönetici haklarından kullanıcı hesabına geri dön."
        )
    permission = "can_delete_messages"
    m = await adminsOnly(permission, message)
    if m == 1:
        return
    checking = message.from_user.mention
    chat_id = message.chat.id
    if not await is_active_chat(chat_id):
        return await message.reply_text(
            "❌ __**Sesli sohbette bir şeyin duraklatıldığını sanmıyorum**__"
        )
    elif await is_music_playing(chat_id):
        return await message.reply_text(
            "❌ __**Sesli sohbette bir şeyin duraklatıldığını sanmıyorum**__"
        )
    else:
        await music_on(chat_id)
        await calls.pytgcalls.resume_stream(chat_id)
        await message.reply_text(
            f"• Devem ettiren : {checking}"
        )


@Client.on_message(command(["son"]) & other_filters)
async def stop(app: Client, message: Message):
    if message.sender_chat:
        return await message.reply_text(
            "🔴 __Siz bir **Anonim Yöneticisiniz**!__\n│\n╰ Yönetici haklarından kullanıcı hesabına geri dön."
        )
    permission = "can_delete_messages"
    m = await adminsOnly(permission, message)
    if m == 1:
        return
    checking = message.from_user.mention
    chat_id = message.chat.id
    if await is_active_chat(chat_id):
        try:
            clear(chat_id)
        except QueueEmpty:
            pass
        await remove_active_chat(chat_id)
        await calls.pytgcalls.leave_group_call(chat_id)
        await message.reply_text(
            f"• Sonlandıran: {checking}"
        )
    else:
        return await message.reply_text(
            "❌ __**Sesli sohbette bir şey çalıyor mu bilmiyorum**__"
        )


@Client.on_message(command(["atla"]) & other_filters)
async def skip(app: Client, message: Message):
    if message.sender_chat:
        return await message.reply_text(
            "🔴 __Siz bir **Anonim Yöneticisiniz**!__\n│\n╰ Yönetici haklarından kullanıcı hesabına geri dön."
        )
    permission = "can_delete_messages"
    m = await adminsOnly(permission, message)
    if m == 1:
        return
    checking = message.from_user.mention
    chat_id = message.chat.id
    chat_title = message.chat.title
    if not await is_active_chat(chat_id):
        await message.reply_text("❌ __**Sesli sohbette hiçbir şey çalmıyor**__")
    else:
        task_done(chat_id)
        if is_empty(chat_id):
            await remove_active_chat(chat_id)
            await message.reply_text(
                "❌ __**Sırada artık müzik yok**__\n\n**»** `Sesli Sohbetten Ayrılıyorum...`"
            )
            await calls.pytgcalls.leave_group_call(chat_id)
            return
        else:
            await calls.pytgcalls.change_stream(
                chat_id,
                InputStream(
                    InputAudioStream(
                        get(chat_id)["file"],
                    ),
                ),
            )
            await message.reply_text(
                f"• Atlatan : {checking}"
            )


@Client.on_message(filters.command(["temizle"]))
async def stop_cmd(app: Client, message):
    if message.sender_chat:
        return await message.reply_text(
            "🔴 __Siz bir **Anonim Yöneticisiniz**!__\n│\n╰ Yönetici haklarından kullanıcı hesabına geri dön."
        )
    permission = "can_delete_messages"
    m = await adminsOnly(permission, message)
    if m == 1:
        return
    chat_id = message.chat.id
    checking = message.from_user.mention
    try:
        clear(chat_id)
    except QueueEmpty:
        pass
    await remove_active_chat(chat_id)
    try:
        await calls.pytgcalls.leave_group_call(chat_id)
    except:
        pass
    await message.reply_text(
        f"✅ __Silinen sıralar **{message.chat.title}**__\n│\n╰ Temizleyen {checking}"
    )
