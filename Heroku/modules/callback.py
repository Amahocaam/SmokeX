from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

from Heroku.config import BOT_NAME, OWNER_USERNAME, UPDATE, SUPPORT, BOT_USERNAME

HELP_TEXT = """
Selam [{}](tg://user?id={})
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
✘ ✘ Merhaba ben Monster Müzik 🇹🇷
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
                        "📚 Komutlar", callback_data="komut")
                ]
           ]
        ),
    )



@Client.on_callback_query(filters.regex("komut"))
async def cbkomut(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""ʜᴇʏʏ [{query.message.chat.first_name}](tg://user?id={query.message.chat.id})
ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ɢɪᴠᴇɴ ʙᴇʟᴏᴡ ᴛᴏ ᴋɴᴏᴡ ᴍᴏʀᴇ ᴀʙᴏᴜᴛ ᴍᴇ :""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Ana Bot", url=f"https://heroku.com"),
                    InlineKeyboardButton(
                        "👤 Owner", url=f"https://github.com/Itz-Zaid")
                ],
                [
                    InlineKeyboardButton(
                        "📚 Komutlar", callback_data="credit"),
                    InlineKeyboardButton(
                        "❄️ Bot yapımı", callback_data="clonebot")
                ],
                [
                    InlineKeyboardButton("⬅️ Geri", callback_data="home")
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
                    InlineKeyboardButton("⬅️ Geri", callback_data="komut")
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


@Client.on_callback_query(filters.regex("clonebot"))
async def clonebot(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""Sizde Kendinize Özel Bot Mu Yapmak İstiyorsunuz? O Zaman Doğru Yerdesin. 

Müzik Botu Yapma:
/clone BOT_TOKEN

Örnek:
/clone 1234567890:SJYEKFNALFKALCMAMXK


Bu Sayede Grubunuz İçin Müzik Botu Yapabilirsiniz.""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("⬅️ Geri", callback_data="komut")
                ],
            ]
        ),
    )

