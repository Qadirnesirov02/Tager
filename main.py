from pyrogram import Client, filters, emoji
from pyrogram.types import Message, Chat, InlineKeyboardMarkup, InlineKeyboardButton, ChatPermissions
import sys
import os
import time

API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
BOT_NAME = os.getenv("BOT_NAME")



TG = Client(
	"TagAll Bot",
	api_id=API_ID,
	api_hash=API_HASH,
	bot_token=BOT_TOKEN
	)

MENTION = "[{}](tg://user?id={})"
MESSAGE = "Salam! {}, Əyləncə Dolu Qrupumuza Xoş Gəldin🥳!Qaydalara riayət etdikcə səndə favori userlərimizdən biri olacaqsan🤩! Əminəm ki Nümunəvi Userlərdən biri olacaqsan!🥰"

DUR = False
SORGU = None
WSORGU = None
WDUR = False

GRUP = []


def bstart():
	BUTTON=[[InlineKeyboardButton(text="👨🏻‍💻 Sahibim", url="https://t.me/nesirovqadirofficiall")]]
	BUTTON+=[[InlineKeyboardButton(text="Məni Qrupa Əlavə Et ✅", url=f"https://t.me/ayparatager_bot?startgroup=true")]]
	return InlineKeyboardMarkup(BUTTON)

def btag():
	BUTTON=[[InlineKeyboardButton(text="👨🏻‍💻 Sahibim", url="https://t.me/nesirovqadirofficiall")]]
	BUTTON=[[InlineKeyboardButton(text="SEVGİMSEN", url="https://t.me/sevgimsende")]]
	return InlineKeyboardMarkup(BUTTON)

@TG.on_message(
	filters.command("start")
	& filters.private
	)
async def start(client, message):
	if message.chat.id != GRUP:
		GRUP.append(message.chat.id)
	else:
		pass
	await message.reply_text(f"Salam! {message.from_user.mention}\n\nMən [@nesirovqadirofficiall](https://t.me/nesirovqadirofficiall) tərəfindən hazırlanan tag botuyam!⚡️\n\nKomutlarla Bağlı Məlumat üçün /help yaz!🥰",
		disable_web_page_preview=True,
		reply_markup=bstart()
		)
@TG.on_message(
	filters.command(["start", f"start@{BOT_NAME}"])
	& filters.group
	)
async def star(client, message):
	if message.chat.id != GRUP:
		GRUP.append(message.chat.id)
	else:
		pass
	await message.reply_text(f"Salam! {message.from_user.mention}\n\nMən [@nesirovqadirofficiall](https://t.me/nesirovqadirofficiall) tərəfindən hazırlanan tag botuyam!⚡️\n\nKomutlarla Bağlı Məlumat üçün /help yaz!🥰",
		disable_web_page_preview=True,
		reply_markup=bstart()
		)
	
@TG.on_message(
	filters.command(["help", f"help@{BOT_NAME}"])
	& filters.group
)
async def help(client, message):
	await message.reply_text(f"Salam!{message.from_user.mention}\n\nƏmrlərlə Bağlı Kömək menyusundasınız➡️Əmrlərin İstifadəsi:\n/admin Qrupdakı Bütün adminləri tag edir✅\n/all Qrupdakı hərkəsi tag edir✅\n/cancel Tag prosesini dayandırır✅\n\nHəmçini Bot’da Qrupa Gələn şəxsləri Salamlama funksiyası vardır🥰\n\nDiqqət!:Əgər Qrupda Admin deyilsəniz bu funksiyalar sizdə işləmiyəcək!❌")
	
@TG.on_message(
	filters.command("help")
	& filters.private
)
async def hel(client, message):
	await message.reply_text(f"Salam!{message.from_user.mention}\n\nƏmrlərlə Bağlı Kömək menyusundasınız➡️Əmrlərin İstifadəsi:\n/admin Qrupdakı Bütün adminləri tag edir✅\n/all Qrupdakı hərkəsi tag edir✅\n/cancel Tag prosesini dayandırır✅\n\nHəmçini Bot’da Qrupa Gələn şəxsləri Salamlama funksiyası vardır🥰\n\nDiqqət!:Əgər Qrupda Admin deyilsəniz bu funksiyalar sizdə işləmiyəcək!❌")
	
@TG.on_message(
	filters.command(["admin", "all"])
	& filters.private
)
async def priw(client, message):
	await message.reply_text("Hmm burada 2miz olduğumuz üçün və 2 mizdə online olduğumuz üçün bu əmri qruplarda işlət!🤠")


@TG.on_message(
	filters.command("all")
	& filters.group
	)
async def tag(client: TG, message: Message):
	global DUR
	global SORGU
	msg = " ".join(message.command[1:])
	chat = message.chat
	async for mem in TG.iter_chat_members(chat_id=chat.id, filter="administrators"):
		if message.from_user.id == mem.user.id:
			await message.reply_text(f"{message.from_user.mention} Tag Prosesini Başlatdı! Hərkəsi Tag Edirəm Boss!⚡️",
				reply_markup=btag()
				)
			time.sleep(1)
			SORGU = True
			async for member in TG.iter_chat_members(chat_id=chat.id, filter="all"):
				if DUR:
					DUR=False
					SORGU = None
					break
				time.sleep(1)
				await TG.send_message(chat_id=chat.id, text=f"{member.user.mention} {msg}")
				time.sleep(1.5)
		if message.from_user.id != mem.user.id:
			pass
		
@TG.on_message(
	filters.command("admin")
	& filters.group
	)
async def ta(client: TG, message: Message):
	global DUR
	global SORGU
	msg = " ".join(message.command[1:])
	chat = message.chat
	async for mem in TG.iter_chat_members(chat_id=chat.id, filter="administrators"):
		if message.from_user.id == mem.user.id:
			await message.reply_text(f"{message.from_user.mention} Adminləri tag etməyimi istədi⚡️ Adminləri Tag Edirəm Boss!🥳",
				reply_markup=btag()
				)
			time.sleep(1)
			SORGU = True
			async for member in TG.iter_chat_members(chat_id=chat.id, filter="administrators"):
				if DUR:
					DUR=False
					SORGU = None
					break
				time.sleep(1)
				await TG.send_message(chat_id=chat.id, text=f"{member.user.mention} {msg}")
				time.sleep(1.5)
		if message.from_user.id != mem.user.id:
			pass


		
@TG.on_message(
	filters.group
	& filters.command("cancel")
)
async def stop(client: TG, message: Message):
	global DUR
	chat = message.chat
	async for mem in TG.iter_chat_members(chat_id=chat.id, filter="administrators"):
		if message.from_user.id == mem.user.id:
			if SORGU == None:
				await message.reply_text("Aktiv bir all prosesi yoxdur😕👍🏻")
				return

			DUR = True
			await message.reply_text(f"{message.from_user.mention} Tag prosesini dayandırdı❌ Tamam heçkəsi tag etmirəm😒")	
		if message.from_user.id != mem.user.id:
			pass
		

@TG.on_message(
	filters.command("reklam")
	& filters.private
	)
async def duyuru(client: TG, message: Message):
	text = " ".join(message.command[1:])
	if message.from_user.id == 1340618002:
		for i in GRUP:
			await TG.send_message(chat_id=i, text=f"Yeni Reklam:\n{text}")
	else:
		await message.reply_text("<b>Sən sudo deyilsen qaqaşım.</b>")


@TG.on_message(filters.group & filters.new_chat_members)
def welcome(client, message):
	global WDUR
	global WSORGU
	WSORGU=True
	for i in message.new_chat_members:
		new_members = MENTION.format(i.first_name, i.id)
		text = MESSAGE.format(new_members)
		message.reply(text, disable_web_page_preview=True)
	
TG.run()
