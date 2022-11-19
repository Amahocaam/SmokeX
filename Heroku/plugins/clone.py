import os
import re
import asyncio
import time
from pyrogram import *
from pyrogram.types import *
from random import choice
from Heroku import cloner, ASSUSERNAME, BOT_NAME
from Heroku.config import API_ID, API_HASH
IMG = ["https://telegra.ph/file/cefd3211a5acdcd332415.jpg", "https://telegra.ph/file/30d743cea510c563af6e3.jpg", "https://telegra.ph/file/f7ae22a1491f530c05279.jpg", "https://telegra.ph/file/2f1c9c98452ae9a958f7d.jpg"]
MESSAGE = "Heya! I'm a music bot hoster/Cloner\n\nI can Host Your Bot On My Server within seconds\n\nTry /clone Token from @botfather"

@cloner.on_message(filters.private & filters.command("dkkdej"))
async def hello(client, message: Message):
    buttons = [
           [
                InlineKeyboardButton("✘ ᴜᴘᴅᴀᴛᴇꜱ ᴄʜᴀɴɴᴇʟ", url="t.me/TheUpdatesChannel"),
            ],
            [
                InlineKeyboardButton("✘ ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ", url="t.me/TheSupportChat"),
            ],
            ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await client.send_photo(message.chat.id, f"{choice(IMG)}", caption=MESSAGE, reply_markup=reply_markup)

##Copy from here 

# © By Itz-Zaid Your motherfucker if uh Don't gives credits.
@cloner.on_message(filters.private & filters.command("clone"))
async def clone(bot, msg: Message):
    chat = msg.chat
    text = await msg.reply("Kullanım:\n\n /clone token")
    cmd = msg.command
    phone = msg.command[1]
    try:
        await text.edit("Yükleniyor... ")
                   # change this Directry according to ur repo
        client = Client(":memory:", API_ID, API_HASH, bot_token=phone, plugins={"root": "Heroku.modules"})
        await client.start()
        user = await client.get_me()
        await msg.reply(f"Başarıyla Başlatıldı @{user.username}! ✅ \n\n Şimdi Botunuzu ve Asistanı @{ASSUSERNAME} Grubunuza Ekleyin!")
    except Exception as e:
        await msg.reply(f"**HATA:** `{str(e)}`\nYeniden /start veriniz.")
#End
##This code fit with every pyrogram Codes just import then @Client Xyz!

