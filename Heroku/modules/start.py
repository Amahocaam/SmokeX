import asyncio

from pyrogram import Client, filters, __version__ as pyrover
from pyrogram.errors import FloodWait, UserNotParticipant
from pytgcalls import (__version__ as pytover)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, ChatJoinRequest

from time import time
from datetime import datetime

from Heroku.setup.filters import command
from Heroku.config import BOT_NAME, OWNER_USERNAME, UPDATE, SUPPORT, BOT_USERNAME

START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 * 60 * 24),
    ("hour", 60 * 60),
    ("min", 60),
    ("sec", 1),
)

HELP_TEXT = """
Selam {}
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
✘ Merhaba ben Monster Müzik 🇹🇷
‣ Grubunuzda müzik müzik oynatabilirim.
‣ Beni gruba yönetici olarak ekleyin ve kesintisiz müziğin tadını çıkarın.
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
"""


@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_text(f"{HELP_TEXT}".format(message.from_user.mention()),
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


@Client.on_message(command(["ping"]) & ~filters.edited)
async def ping_pong(client: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("ᴘɪɴɢ..... 👀")
    delta_ping = time() - start
    await m_reply.edit_text("Pong.... \n" f"`{delta_ping * 1000:.3f} ᴍs`")
