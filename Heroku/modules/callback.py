from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

from Heroku.config import BOT_NAME, OWNER_USERNAME, UPDATE, SUPPORT, BOT_USERNAME

HELP_TEXT = """
Selam [{}](tg://user?id={})
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
✘ ✘ Merhaba ben 𝙂𝙧𝙪𝙥 𝙈𝙪̈𝙯𝙞𝙠 🇹🇷
‣ Grubunuzda müzik müzik oynatabilirim.
‣ Beni gruba yönetici olarak ekleyin ve kesintisiz müziğin tadını çıkarın.
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
"""


@Client.on_callback_query(filters.regex("home"))
async def home(_, query: CallbackQuery):
    await query.edit_message_text(f"{HELP_TEXT}".format(query.message.chat.first_name, query.message.chat.id),
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✚ Beni Gruba Ekle", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ],
                [
                    InlineKeyboardButton(
                        "💭 Support", url=f"https://t.me/destekgroup"),
                    InlineKeyboardButton(
                        "📚 Komutlar", callback_data="others")
                ]
           ]
        ),
    )






@Client.on_callback_query(filters.regex("others"))
async def others(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""ʜᴇʏʏ [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) İşte Tüm Komutlar 🇹🇷\n\n» /oynat => <Şarkı İsmi> Müzik oynatır.\n» /durdur => Müziği dururur.\n» /devam => Müziği sürdürür.\n» /atla => Müziği atlar.\n» /son => Müziği sonlandırır.\n» /bul => Müzik indirir.\n» /katil => Asistanı gruba davet eder.""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🛠️ Kaynak Kod", url=f"https://te.legra.ph/file/bd12f1d8d0a2e893d056c.jpg"),
                    InlineKeyboardButton(
                        "💝 Owner", url=f"https://t.me/emilyboss")
                ],
                [
                    InlineKeyboardButton("⬅️ Geri", callback_data="home")
                ]
           ]
        ),
    )


@Client.on_callback_query(filters.regex("credit"))
async def credit(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""İşte Tüm Komutlar 🇹🇷\n\n» /oynat => <Şarkı İsmi> Müzik oynatır.\n» /durdur => Müziği dururur.\n» /devam => Müziği sürdürür.\n» /atla => Müziği atlar.\n» /son => Müziği sonlandırır.\n» /bul => Müzik indirir.\n» /katil => Asistanı gruba davet eder.""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("🗑️ Kapat", callback_data="cls")
                ],
            ]
        ),
    )

@Client.on_callback_query(filters.regex("cls"))
async def reinfo(_, query: CallbackQuery):
    try:
        await query.message.delete()
        await query.message.reply_to_message.delete()
    except Exception:
        pass


@Client.on_callback_query(filters.regex("repoinfo"))
async def repoinfo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""ᴀʙᴏᴜᴛ ᴛʜᴇ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ : 

ᴛʜɪs ʀᴇᴘᴏ ɪs ᴏɴʟʏ ᴍᴀᴅᴇ ғᴏʀ ᴅᴇᴘʟᴏʏɪɴɢ ᴀ ᴘᴏᴡᴇʀғᴜʟ ᴍᴜsɪᴄ ʙᴏᴛ ᴏɴ ʜᴇʀᴏᴋᴜ ᴡɪᴛʜᴏᴜᴛ ғᴀᴄɪɴɢ ʜᴇʀᴏᴋᴜ ᴀᴄᴄᴏᴜɴᴛ ʙᴀɴɴɪɴɢ ᴘʀᴏʙᴇʟᴍ.

🔗 sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ : https://github.com/ITZ-ZAID/Zaid-Vc-Player""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("⬅️ ʙᴀᴄᴋ", callback_data="others")
                ],
            ]
        ),
        disable_web_page_preview=True,
    )
