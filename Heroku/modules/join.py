import asyncio

from pyrogram import Client, filters
from pyrogram.errors import UserAlreadyParticipant, FloodWait

from Heroku import ASSUSERNAME
from Heroku.setup.decorators import sudo_users_only, errors
from Heroku.setup.administrator import adminsOnly
from Heroku.setup.filters import command
from Heroku.calls import client as USER


@Client.on_message(
    command(["katil", "gel", "orispi"]) & ~filters.private & ~filters.bot
)
@errors
async def addchannel(client, message):
    if message.sender_chat:
        return await message.reply_text(
            "🔴 __Siz bir **Anonim Yöneticisiniz**!__\n│\n╰ Yönetici haklarından kullanıcı hesabına geri dön."
        )
    permission = "can_delete_messages"
    m = await adminsOnly(permission, message)
    if m == 1:
        return
    chid = message.chat.id
    try:
        invite_link = await message.chat.export_invite_link()
        if "+" in invite_link:
            kontol = (invite_link.replace("+", "")).split("t.me/")[1]
            link_bokep = f"https://t.me/joinchat/{kontol}"
    except:
        await message.reply_text(
            "**önce beni admin yap**",
        )
        return

    try:
        user = await USER.get_me()
    except:
        user.first_name = f"{ASSUSERNAME}"

    try:
        await USER.join_chat(link_bokep)
    except UserAlreadyParticipant:
        await message.reply_text(
            f"🔴 **{user.first_name} bu gruba zaten katıldı !!**",
        )
    except Exception as e:
        print(e)
        await message.reply_text(
            f"❌ **Assistant ({user.first_name}) userbot için birçok katılma isteği nedeniyle grubunuza katılamıyor!**\n‼️ Kullanıcının grupta yasaklanmadığından emin olun."
            f"\n\n» `Manuel olarak ekleyin {user.first_name} gruba`",
        )
        return


@USER.on_message(filters.group & command(["ayril", "git", "sg"]))
async def rem(USER, message):
    if message.sender_chat:
        return await message.reply_text(
            "🔴 __Siz bir **Anonim Yöneticisiniz**!__\n│\n╰ Yönetici haklarından kullanıcı hesabına geri dön."
        )
    permission = "can_delete_messages"
    m = await adminsOnly(permission, message)
    if m == 1:
        return
    try:
        await USER.send_message(
            message.chat.id,
            "✅ userbot sohbetten ayrıldı....",
        )
        await USER.leave_chat(message.chat.id)
    except:
        await message.reply_text(
            "❌ **Asistan grubunuzdan ayrılamaz!**\n\n» Beni grubunuzdan manuel olarak çıkarın</b>"
        )

        return


@Client.on_message(command(["gece", "leaveall"]))
@sudo_users_only
async def bye(client, message):
    left = 0
    sleep_time = 0.1
    lol = await message.reply("**Asistan tüm gruplardan ayrılıyor**\n\n`Bekleyiniz...`")
    async for dialog in USER.iter_dialogs():
        try:
            await USER.leave_chat(dialog.chat.id)
            await asyncio.sleep(sleep_time)
            left += 1
        except FloodWait as e:
            await asyncio.sleep(int(e.x))
        except Exception:
            pass
    await lol.edit(f"🏃‍♂️ `Asistan ayrılıyor...`\n\n» **Left:** {left} chats.")
