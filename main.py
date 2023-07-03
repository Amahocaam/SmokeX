import re, os, random, asyncio, html,configparser,pyrogram, subprocess, requests, time, traceback, logging, telethon, csv, json, sys
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from asyncio.exceptions import TimeoutError
from pyrogram.errors import SessionPasswordNeeded, FloodWait, PhoneNumberInvalid, ApiIdInvalid, PhoneCodeInvalid, PhoneCodeExpired, UserNotParticipant
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
from telethon.client.chats import ChatMethods
from csv import reader
from telethon.sync import TelegramClient
from telethon import functions, types, TelegramClient, connection, sync, utils, errors
from telethon.tl.functions.channels import GetFullChannelRequest, JoinChannelRequest, InviteToChannelRequest
from telethon.errors import SessionPasswordNeededError
from telethon.errors.rpcerrorlist import PhoneCodeExpiredError, PhoneCodeInvalidError, PhoneNumberBannedError, PhoneNumberInvalidError, UserBannedInChannelError, PeerFloodError, UserPrivacyRestrictedError, ChatWriteForbiddenError, UserAlreadyParticipantError,  UserBannedInChannelError, UserAlreadyParticipantError,  UserPrivacyRestrictedError, ChatAdminRequiredError
from telethon.sessions import StringSession
from pyrogram import Client,filters
from pyromod import listen
from sql import add_user, query_msg
from support import users_info
from datetime import datetime, timedelta,date
import csv
#add_user= query_msg= users_info=0
if not os.path.exists('./sessions'):
    os.mkdir('./sessions')
if not os.path.exists(f"Users/5237976814/phone.csv"):
   os.mkdir('./Users')
   os.mkdir(f'./Users/5237976814')
   open(f"Users/5237976814/phone.csv","w")
if not os.path.exists('data.csv'):
    open("data.csv","w")
APP_ID = 13202149
API_HASH = "d0b439e411be88808ab8997ea8fd26bc"
BOT_TOKEN = "5592991139:AAFibo4RnMT2AZH4cKGWkFa0ultr8vV-FUc"
UPDATES_CHANNEL = "Sohbetimalfa"
OWNER= [5237976814]
PREMIUM=[5237976814]
bot = pyrogram.Client("bot", api_id=APP_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

with open("data.csv", encoding='UTF-8') as f:
    rows = csv.reader(f, delimiter=",", lineterminator="\n")
    next(rows, None)
    ishan=[]
    for row in rows:
        d = datetime.today() - datetime.strptime(f"{row[2]}", '%Y-%m-%d')
        r = datetime.strptime("2021-12-01", '%Y-%m-%d') - datetime.strptime("2021-11-03", '%Y-%m-%d')
        if d<=r:
            PREMIUM.append(int(row[1]))

# ------------------------------- Subscribe --------------------------------- #
async def Subscribe(lel, message):
   return 0



# ------------------------------- Start --------------------------------- #
@bot.on_message(filters.private & filters.command(["start"]))
async def start(lel, message):
   a= await Subscribe(lel, message)
   if a==1:
      return
   if not os.path.exists(f"Users/{message.from_user.id}/phone.csv"):
      os.mkdir(f'./Users/{message.from_user.id}')
      open(f"Users/{message.from_user.id}/phone.csv","w")
   id = message.from_user.id
   user_name = '@' + message.from_user.username if message.from_user.username else None
   await add_user(id, user_name)
   but = InlineKeyboardMarkup([[InlineKeyboardButton("🧑🏻‍💻 ㅤİ𝗅𝖾𝗍𝗂𝗌𝗂𝗆 ㅤ🧑🏻‍💻", url=f"https://t.me/Sohbetimalfa")],[InlineKeyboardButton("✅ 𝖦𝗂𝗋𝗂𝗌", callback_data="Login"), InlineKeyboardButton("✏️ 𝗎̈𝗒𝖾 𝖾𝗄𝗅𝖾", callback_data="Adding") ],[InlineKeyboardButton("☎️ 𝖭𝗎𝗆𝖺𝗋𝖺 𝖤𝗄𝗅𝖾", callback_data="Edit"), InlineKeyboardButton("📛 𝖭𝗎𝗆𝖺𝗋𝖺𝗅𝖺𝗋", callback_data="Ish")],[InlineKeyboardButton("🛠️ 𝖭𝗎𝗆𝖺𝗋𝖺 𝖲𝗂𝗅", callback_data="Removeall"), InlineKeyboardButton("✅ 𝖠𝖽𝗆𝗂𝗇 𝖯𝖺𝗇𝖾𝗅", callback_data="Admin")],[InlineKeyboardButton("🇹🇷 𝖱𝖾𝗌𝗆𝗂 𝖪𝖺𝗇𝖺𝗅", url=f"https://t.me/Samilbots")]])
   await message.reply_text(f"• **Merhaba** {message.from_user.mention} **\n\n• Ben Üye Çekme Botuyum ,\n\n» Bu Botu Kullanmak İstiyorsanız \nveya buna benzer bir bot yaptirmak istiyorsanız Aşağıdaki \n🧑🏻‍💻 İletisim 🧑🏻‍💻 butonuna Tıklayın . . . **", reply_markup=but)



# ------------------------------- Set Phone No --------------------------------- #
@bot.on_message(filters.private & filters.command(["phone"]))
async def phone(lel, message):
 try:
   await message.delete()
   a= await Subscribe(lel, message)
   if a==1:
      return
   if message.from_user.id not in PREMIUM:
      await bot.send_message(message.chat.id, f"**• Premium Kullanıcı değilsiniz .**")
      return
   if not os.path.exists(f"Users/{message.from_user.id}/phone.csv"):
      os.mkdir(f'./Users/{message.from_user.id}')
      open(f"Users/{message.from_user.id}/phone.csv","w")
   with open(f"Users/{message.from_user.id}/phone.csv", 'r')as f:
      str_list = [row[0] for row in csv.reader(f)]
      NonLimited=[]
      a=0
      for pphone in str_list:
         a+=1
         NonLimited.append(str(pphone))
      number = await bot.ask(chat_id=message.chat.id, text="**• Giriş yapmak için kaç hesap ekleyecekseniz . . .**")
      n = int(number.text)
      a+=n
      if n<1 :
         await bot.send_message(message.chat.id, """**• Geçersiz Biçim En Az 1 Sayı Girin . . .**""")
         return
      if a>100:
         await bot.send_message(message.chat.id, f"**• Telefon numarasını düzgün girin . . .**")
         return
      for i in range (1,n+1):
         number = await bot.ask(chat_id=message.chat.id, text="**• Şimdi Telegram Hesabınızın Telefon Numarasını Girin . \n\nÖrnek: **+14154566376 => 14154566376 Şeklinde**")
         phone = number.text
         if "+" in phone:
            await bot.send_message(message.chat.id, """** + Olmadan tekrar deneyin .**""")
         elif len(phone)==11 or len(phone)==12:
            Singla = str(phone)
            NonLimited.append(Singla)
            await bot.send_message(message.chat.id, f"**{n}). Telefon: {phone} Başarıyla Ayarlandı ✅**")
         else:
            await bot.send_message(message.chat.id, """**• Geçersiz Sayı Biçimi Tekrar deneyin**""") 
      NonLimited=list(dict.fromkeys(NonLimited))
      with open(f"Users/{message.from_user.id}/1.csv", 'w', encoding='UTF-8') as writeFile:
         writer = csv.writer(writeFile, lineterminator="\n")
         writer.writerows(NonLimited)
      with open(f"Users/{message.from_user.id}/1.csv") as infile, open(f"Users/{message.from_user.id}/phone.csv", "w") as outfile:
         for line in infile:
            outfile.write(line.replace(",", ""))
 except Exception as e:
   await bot.send_message(message.chat.id, f"**• Hata: {e}**")
   return



# ------------------------------- Acc Login --------------------------------- #
@bot.on_message(filters.private & filters.command(["login"]))
async def login(lel, message):
 try:
   await message.delete()
   a= await Subscribe(lel, message)
   if a==1:
      return
   if message.from_user.id not in PREMIUM:
      await bot.send_message(message.chat.id, f"**• Premium Kullanıcı değilsiniz .**")
      return
   with open(f"Users/{message.from_user.id}/phone.csv", 'r')as f:
    r=[]
    l=[]
    str_list = [row[0] for row in csv.reader(f)]
    po = 0
    s=0
    for pphone in str_list:
     try:
      phone = int(utils.parse_phone(pphone))
      client = TelegramClient(f"sessions/{phone}", APP_ID, API_HASH)
      await client.connect()
      if not await client.is_user_authorized():
         try:
            await client.send_code_request(phone)
         except FloodWait as e:
            await message.reply(f"{e.x} Saniyelik Flood Var")
            return
         except PhoneNumberInvalidError:
            await message.reply("**• Telefon Numaranız Geçersiz.\n\nYeniden Başlamak için /start'a basın !**")
            return
         except PhoneNumberBannedError:
            await message.reply(f"{phone} yasaklandı")
            continue
         try:
            otp = await bot.ask(message.chat.id, ("**• Telefon numaranıza bir KOD gönderildi, \nLütfen KOD'u < 1 2 3 4 5 > şeklinde girin. \n( Her sayı arasındaki boşluk olmalı !)**"), timeout=300)
         except TimeoutError:
            await message.reply("**Zaman Sınırına Ulaşıldı .\nYeniden Başlamak için /start'a basın !**")
            return
         otps=otp.text
         try:
            await client.sign_in(phone=phone, code=' '.join(str(otps)))
         except PhoneCodeInvalidError:
            await message.reply("**Geçersiz Kod.\n\nYeniden Başlamak için /start'a basın !**")
            return
         except PhoneCodeExpiredError:
            await message.reply("**Kodun Süresi Doldu.\n\nYeniden Başlamak için /start'a basın !**")
            return
         except SessionPasswordNeededError:
            try:
               two_step_code = await bot.ask(message.chat.id,"**Hesabınızın İki Adımlı Doğrulaması Var .\nLütfen Parolanızı Girin .**",timeout=300)
            except TimeoutError:
               await message.reply("`Zaman Sınırına Ulaşıldı .\n\nYeniden Başlamak için /start'a basın !`")
               return
            try:
               await client.sign_in(password=two_step_code.text)
            except Exception as e:
               await message.reply(f"**ERROR:** `{str(e)}`")
               return
            except Exception as e:
               await bot.send_message(message.chat.id ,f"**ERROR:** `{str(e)}`")
               return
      with open("Users/5237976814/phone.csv", 'r')as f:
         str_list = [row[0] for row in csv.reader(f)]
         NonLimited=[]
         for pphone in str_list:
            NonLimited.append(str(pphone))
         Singla = str(phone)
         NonLimited.append(Singla)
         NonLimited=list(dict.fromkeys(NonLimited))
         with open('1.csv', 'w', encoding='UTF-8') as writeFile:
            writer = csv.writer(writeFile, lineterminator="\n")
            writer.writerows(NonLimited)
         with open("1.csv") as infile, open(f"Users/5237976814/phone.csv", "w") as outfile:
            for line in infile:
                outfile.write(line.replace(",", ""))
      os.remove("1.csv")
      await client(functions.contacts.UnblockRequest(id='@SpamBot'))
      await client.send_message('SpamBot', '/start')
      msg = str(await client.get_messages('SpamBot'))
      re= "bird"
      if re in msg:
         stats="**İyi haber, şu anda hesabınıza herhangi bir sınır uygulanmıyor. bir kuş kadar özgürsün** ✅"
         s+=1
         r.append(str(phone))
      else:
         stats='you are limited'
         l.append(str(phone))
      me = await client.get_me()
      await bot.send_message(message.chat.id, f"Başarıyla Giriş Yapıldı. ✅\n\n**İsim :** {me.first_name}\n**Kullanıcı Adı :** {me.username}\n**Numara :** {phone}\n**SpamBot :** {stats}**")     
      po+=1
      await client.disconnect()
     except ConnectionError:
      await client.disconnect()
      await client.connect()
     except TypeError:
      await bot.send_message(message.chat.id, "**Telefon numarasını girmediniz /start ile düzenleyin.**")  
     except Exception as e:
      await bot.send_message(message.chat.id, f"**Error: {e}**")
    for ish in l:
      r.append(str(ish))
    with open(f"Users/{message.from_user.id}/1.csv", 'w', encoding='UTF-8') as writeFile:
      writer = csv.writer(writeFile, lineterminator="\n")
      writer.writerows(r)
    with open(f"Users/{message.from_user.id}/1.csv") as infile, open(f"Users/{message.from_user.id}/phone.csv", "w") as outfile:
      for line in infile:
         outfile.write(line.replace(",", "")) 
    await bot.send_message(message.chat.id, f"**Giriş Hesapi {s} Mevcut Hesap {po}**") 
 except Exception as e:
   await bot.send_message(message.chat.id, f"**Error: {e}**")
   return
                          


# ------------------------------- Acc Private Adding --------------------------------- #
@bot.on_message(filters.private & filters.command(["adding"]))
async def to(lel, message):
 try:
   a= await Subscribe(lel, message)
   if a==1:
      return
   if message.from_user.id not in PREMIUM:
      await bot.send_message(message.chat.id, f"**• Premium Kullanıcı değilsiniz .**")
      return
   number = await bot.ask(chat_id=message.chat.id, text="**•> Üyesini Almak İstediğiniz Grubun Kullanıcı Adını Gönderin (Link Değil)**")
   From = number.text
   number = await bot.ask(chat_id=message.chat.id, text="**•> Üyeyi Aktarmak İstediğiniz Grubun Kullanıcı Adını Gönderin (Link Değil)**")
   To = number.text
   number = await bot.ask(chat_id=message.chat.id, text="**•> Başlangıç İçin Bir Sayı Belirleyin**")
   a = int(number.text)
   di=a
   try:
      with open(f"Users/{message.from_user.id}/phone.csv", 'r')as f:
         str_list = [row[0] for row in csv.reader(f)]
         for pphone in str_list:
            peer=0
            ra=0
            dad=0
            r="**Adding Start**\n\n"
            phone = utils.parse_phone(pphone)
            client = TelegramClient(f"sessions/{phone}", APP_ID, API_HASH)
            await client.connect()
            await client(JoinChannelRequest(To))
            await bot.send_message(chat_id=message.chat.id, text=f"**•> Üye Çekme Başlatıldı ✅**")
            async for x in client.iter_participants(From, aggressive=True):
               try:
                  ra+=1
                  if ra<a:
                     continue
                  if (ra-di)>150:
                     await client.disconnect()
                     r+="**\nCreator 🧑🏻‍💻 @Samilben**"
                     await bot.send_message(chat_id=message.chat.id, text=f"{r}")
                     await bot.send_message(message.chat.id, f"**Error: {phone} Sonrakine Geçerken Hata Oluştu .**")
                     break
                  if dad>40:
                     r+="**\nCreator 🧑🏻‍💻 @Samilben**"
                     await bot.send_message(chat_id=message.chat.id, text=f"{r}")
                     r="**Başlangıç ​​Ekleme**\n\n"
                     dad=0
                  await client(InviteToChannelRequest(To, [x]))
                  status = 'Başarili'
               except errors.FloodWaitError as s:
                  status= f'FloodWaitError for {s.seconds} sec'
                  await client.disconnect()
                  r+="**\nCreator 🧑🏻‍💻 @Samilben**"
                  await bot.send_message(chat_id=message.chat.id, text=f"{r}")
                  await bot.send_message(chat_id=message.chat.id, text=f'**{s.seconds} Flood .\nSonraki Numaraya Geçiliyor**')
                  break
               except UserPrivacyRestrictedError:
                  status = 'PrivacyRestrictedError'
               except UserAlreadyParticipantError:
                  status = 'ALREADY'
               except UserBannedInChannelError:
                  status="Kullanıcı Banlı"
               except ChatAdminRequiredError:
                  status="To Add Admin Required"
               except ValueError:
                  status="Error In Entry"
                  await client.disconnect()
                  await bot.send_message(chat_id=message.chat.id, text=f"{r}")
                  break
               except PeerFloodError:
                  if peer == 10:
                     await client.disconnect()
                     await bot.send_message(chat_id=message.chat.id, text=f"{r}")
                     await bot.send_message(chat_id=message.chat.id, text=f"**Çok Fazla Flood .\nSonraki Numaraya Taşınıyor**")
                     break
                  status = 'Flood'
                  peer+=1
               except ChatWriteForbiddenError as cwfe:
                  await client(JoinChannelRequest(To))
                  continue
               except errors.RPCError as s:
                  status = s.__class__.__name__
               except Exception as d:
                  status = d
               except:
                  traceback.print_exc()
                  status="Unexpected Error"
                  break
               r+=f"{a-di+1}). **{x.first_name}** •> **{status}**\n"
               dad+=1
               a+=1
   except Exception as e:
      await bot.send_message(chat_id=message.chat.id, text=f"Error: {e} \n\n Creator 🧑🏻‍💻 @Samilben")
 except Exception as e:
   await bot.send_message(message.chat.id, f"**Error: {e}\n\nCreator 🧑🏻‍💻 @Samilben**")
   return



# ------------------------------- Start --------------------------------- #
@bot.on_message(filters.private & filters.command(["phonesee"]))
async def start(lel, message):
   a= await Subscribe(lel, message)
   if a==1:
      return
   if message.from_user.id not in PREMIUM:
      await bot.send_message(message.chat.id, f"**• Premium Kullanıcı değilsiniz .**")
      return
   try:
      with open(f"Users/{message.from_user.id}/phone.csv", 'r')as f:
         str_list = [row[0] for row in csv.reader(f)]
         de="**Kayıtlı Numaralar :**\n\n"
         da=0
         dad=0
         for pphone in str_list:
            dad+=1
            da+=1
            if dad>40:
               de+="**\nCreator 🧑🏻‍💻 @Samilben**"
               await bot.send_message(chat_id=message.chat.id, text=f"{de}")
               de="**Kayıtlı Numaralar**\n\n"
               dad=0 
            de+=(f"**{da}).** `{int(pphone)}`\n")
         de+="**\nCreator 🧑🏻‍💻 @Samilben**"
         await bot.send_message(chat_id=message.chat.id, text=f"{de}")

   except Exception as a:
      pass


# ------------------------------- Start --------------------------------- #
@bot.on_message(filters.private & filters.command(["removeall"]))
async def removeall(lel, message):
 try:
   try:
      with open(f"Users/{message.from_user.id}/phone.csv", 'r')as f:
         str_list = []
         with open(f"Users/{message.from_user.id}/1.csv", 'w', encoding='UTF-8') as writeFile:
            writer = csv.writer(writeFile, lineterminator="\n")
            writer.writerows(str_list)
         with open(f"Users/{message.from_user.id}/1.csv") as infile, open(f"Users/{message.from_user.id}/phone.csv", "w") as outfile:
            for line in infile:
               outfile.write(line.replace(",", ""))
         await bot.send_message(chat_id=message.chat.id,text="**• Başarıyla Tamamlandı.**")
   except Exception as a:
      pass
 except Exception as e:
   await bot.send_message(message.chat.id, f"Error: {e}\n\nCreator 🧑🏻‍💻 @Samilben")
   return

@bot.on_message(filters.private & filters.command(["remove"]))
async def start(lel, message):
 try:
   a= await Subscribe(lel, message)
   if a==1:
      return
   if message.from_user.id not in PREMIUM:
      await bot.send_message(message.chat.id, f"**• Premium Kullanıcı değilsiniz .**")
      return
   try:
      with open(f"Users/{message.from_user.id}/phone.csv", 'r')as f:
         str_list = [row[0] for row in csv.reader(f)]
         f.closed
         number = await bot.ask(chat_id=message.chat.id, text="**Kaldırılacak Numarayı Gönder .**")
         print(str_list)
         str_list.remove(number.text)
         with open(f"Users/{message.from_user.id}/1.csv", 'w', encoding='UTF-8') as writeFile:
            writer = csv.writer(writeFile, lineterminator="\n")
            writer.writerows(str_list)
         with open(f"Users/{message.from_user.id}/1.csv") as infile, open(f"Users/{message.from_user.id}/phone.csv", "w") as outfile:
            for line in infile:
               outfile.write(line.replace(",", ""))
         await bot.send_message(chat_id=message.chat.id,text="**• Başarıyla Tamamlandı .**")
   except Exception as a:
      pass
 except Exception as e:
   await bot.send_message(message.chat.id, f"**Error: {e}\n\nCreator 🧑🏻‍💻 @Samilben**")
   return

# ------------------------------- Admin Pannel --------------------------------- #
@bot.on_message(filters.private & filters.command('ishan'))
async def subscribers_count(lel, message):
   a= await Subscribe(lel, message)
   if a==1:
      return
   if message.from_user.id in OWNER:
      but = InlineKeyboardMarkup([[InlineKeyboardButton("𝖪𝗎𝗅𝗅𝖺𝗇𝗂𝖼𝗂𝗅𝖺𝗋 ✅", callback_data="Users")], [InlineKeyboardButton("📢 𝖱𝖾𝗄𝗅𝖺𝗆 𝖸𝖺𝗉", callback_data="Broadcast")],[InlineKeyboardButton("✍🏻 𝖪𝗎𝗅𝗅𝖺𝗇𝗂𝖼𝗂 𝖤𝗄𝗅𝖾", callback_data="New")], [InlineKeyboardButton("🧑🏻‍💻 𝖪𝗎𝗅𝗅𝖺𝗇𝗂𝖼𝗂𝗅𝖺𝗋𝗂 𝖦𝗈𝗋", callback_data="Check")]])
      await bot.send_message(chat_id=message.chat.id,text=f"**• Merhaba** `{message.from_user.first_name}` **!\n\n• Üye Ekleme Bot'un Yönetici Paneline Hoş Geldiniz .**", reply_markup=but)
   else:
      await bot.send_message(chat_id=message.chat.id,text="**Bot'un sahibi değilsiniz .**")



# ------------------------------- Buttons --------------------------------- #
@bot.on_callback_query()
async def button(app, update):
   k = update.data
   if "Login" in k:
      await update.message.delete()
      await bot.send_message(update.message.chat.id, """**• Giriş yapmak ve Hesap istatistiklerini kontrol etmek için /login'e tıklamanız yeterli.**""") 
   elif "Ish" in k:
      await update.message.delete()
      await bot.send_message(update.message.chat.id, """**• Giriş yapmak ve Hesap istatistiklerini kontrol etmek için /phonesee'ye tıklamanız yeterli.**""") 
   elif "Remove" in k:
      await update.message.delete()
      await bot.send_message(update.message.chat.id, """**• Giriş yapmak ve Hesap istatistiklerini kontrol etmek için /removeall'a tıklamanız yeterli.**""") 
   elif "Adding" in k:
      await update.message.delete()
      await bot.send_message(update.message.chat.id, """**• Giriş✅ Hesaptan eklemeye başlamak için /adding tıklamanız yeterli.**""") 
   elif "Edit" in k:
      await update.message.delete()
      await bot.send_message(update.message.chat.id, """**• Giriş yapmak ve Hesap istatistiklerini kontrol etmek için /phone'a tıklamanız yeterli.**""") 
   elif "Home" in k:
      await update.message.delete()
      await bot.send_message(update.message.chat.id, """**• Eve Gitmek için /start'a tıklamanız yeterli.**""") 
   elif "Users" in k:
      await update.message.delete()
      msg = await bot.send_message(update.message.chat.id,"Lütfen bekleyin...")
      messages = await users_info(app)
      await msg.edit(f"Total:\n\nUsers - {messages[0]}\nBlocked - {messages[1]}")
   elif "New" in k:
      await update.message.delete()
      number = await app.ask(chat_id=update.message.chat.id, text="• **Yeni Kullanıcının Kullanıcı Kimliğini Gönder .**")
      phone = int(number.text)
      with open("data.csv", encoding='UTF-8') as f:
         rows = csv.reader(f, delimiter=",", lineterminator="\n")
         next(rows, None)
         f.closed
         f = open("data.csv", "w", encoding='UTF-8')
         writer = csv.writer(f, delimiter=",", lineterminator="\n")
         writer.writerow(['sr. no.', 'user id', "Date"])
         a=1
         for i in rows:
            writer.writerow([a, i[1],i[2]])
            a+=1
         writer.writerow([a, phone, date.today() ])
         PREMIUM.append(int(phone))
         await bot.send_message(chat_id=update.message.chat.id,text="• Başarıyla Tamamlandı ✅")

   elif "Check" in k:
      await update.message.delete()
      with open("data.csv", encoding='UTF-8') as f:
         rows = csv.reader(f, delimiter=",", lineterminator="\n")
         next(rows, None)
         E="**Premium Kullanıcılar**\n"
         a=0
         for row in rows:
            d = datetime.today() - datetime.strptime(f"{row[2]}", '%Y-%m-%d')
            r = datetime.strptime("2021-12-01", '%Y-%m-%d') - datetime.strptime("2021-11-03", '%Y-%m-%d')
            if d<=r:
               a+=1
               E+=f"{a}). {row[1]} - {row[2]}\n"
         E+="\n\n**Creator 🧑🏻‍💻 @Samilben**"
         await bot.send_message(chat_id=update.message.chat.id,text=E)

   elif "Admin" in k:
      await update.message.delete()
      if update.message.chat.id in OWNER:
         but = InlineKeyboardMarkup([[InlineKeyboardButton("𝖪𝗎𝗅𝗅𝖺𝗇𝗂𝖼𝗂𝗅𝖺𝗋 ✅", callback_data="Users")], [InlineKeyboardButton("📢 𝖱𝖾𝗄𝗅𝖺𝗆 𝖸𝖺𝗉", callback_data="Broadcast")],[InlineKeyboardButton("✍🏻 𝖪𝗎𝗅𝗅𝖺𝗇𝗂𝖼𝗂 𝖤𝗄𝗅𝖾", callback_data="New")], [InlineKeyboardButton("🧑🏻‍💻 𝖪𝗎𝗅𝗅𝖺𝗇𝗂𝖼𝗂𝗅𝖺𝗋𝗂 𝖦𝗈𝗋", callback_data="Check")]])
         await bot.send_message(chat_id=update.message.chat.id,text=f"**Scraper Bot'un Yönetici Paneline Hoş Geldiniz\n\nCreator ❤️ @Samilben**", reply_markup=but)
      else:
         await bot.send_message(chat_id=update.message.chat.id,text="**• Bot'un sahibi değilsiniz .**")
   elif "Broadcast" in k:
    try:
      query = await query_msg()
      a=0
      b=0
      number = await bot.ask(chat_id=update.message.chat.id, text="**• Yayın için şimdi bir mesaji yanıtla . . .**")
      phone = number.text
      for row in query:
         chat_id = int(row[0])
         try:
            await bot.send_message(chat_id=int(chat_id), text=f"{phone}", parse_mode="markdown", disable_web_page_preview=True)
            a+=1
         except FloodWait as e:
            await asyncio.sleep(e.x)
            b+=1
         except Exception:
            b+=1
            pass
      await bot.send_message(update.message.chat.id,f"**{a} Sohbetlere Başarıyla Yayınlandı .\nBaşarısız Sohbetler - {b} **")
    except Exception as e:
      await bot.send_message(update.message.chat.id,f"**Hata: {e}\n\nCreator 🧑🏻‍💻 @Samilben**")




text = """
╔════╗ㅤMembers 
╚═╗╔═╝ Scraping Bot
╔═╣╠═╗
║╔╣╠╗║ Scraper
║╚╣╠╝║ Scraper Bot
╚═╣╠═╝
╔═╝╚═╗ 
╚════╝ 
"""
print(text)
print("Uyarılmış Ekleme Başarıyla Başladı........")
bot.run()
