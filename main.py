from pyrogram import Client, filters, emoji
from pyrogram.types import Message, Chat, InlineKeyboardMarkup, InlineKeyboardButton, ChatPermissions
import sys
import os
import time

API_ID = os.getenv("API_ID", "19485442")
API_HASH = os.getenv("API_HASH", "a03fcb372b3ec4e406b5d52f84b02e53")
BOT_TOKEN = os.getenv("BOT_TOKEN", "6132791182:AAFrxAmzyg3rpiOdBVGzqQUw1FDbMuIzm_I")
BOT_NAME = os.getenv("BOT_NAME", "ayparatager_bot")



TG = Client(
	"TagAll Bot",
	api_id=API_ID,
	api_hash=API_HASH,
	bot_token=BOT_TOKEN
	)

MENTION = "[{}](tg://user?id={})"
MESSAGE = "Salam! {}, Əyləncə Dolu Qrupumuza Xoş Gəldin🥳! Qaydalara riayət etdikcə səndə favori userlərimizdən biri olacaqsan🤩! Əminəm ki Nümunəvi Userlərdən biri olacaqsan!🥰"

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
	await message.reply_text(f"Salam! {message.from_user.mention}\n\nMən [@nesirovqadirofficiall](https://t.me/nesirovqadirofficiall) tərəfindən hazırlanan tağ botuyam.\n\nKomutlarla bağlı məlumat üçün /help yaz.",
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
	await message.reply_text(f"Salam! {message.from_user.mention}\n\nMən [@nesirovqadirofficiall](https://t.me/nesirovqadirofficiall) tərəfindən hazırlanan tağ botuyam.\n\nKomutlarla bağlı məlumat üçün /help yaz.",
		disable_web_page_preview=True,
		reply_markup=bstart()
		)
	
@TG.on_message(
	filters.command(["help", f"help@{BOT_NAME}"])
	& filters.group
)
async def help(client, message):
	await message.reply_text("**Qrup Admin Əmrləri:**\n🔮 İstifadə: /tag\n📃 Açıqlama: Qrupdakı hərkəsi tağ edər.\n\n🔮 İstifadə: /admin\n📃 Açıqlama: Qrupdakı bütün adminləri tağ edər.\n\n🔮 İstifadə: /cancel\n📃 Açıqlama: Qrupdakı tağ prosesini dayandırar.\n\n**Bot Sahib Əmri:**\n🔮 İstifadə: /reklam\n📃 Açıqlama: Qruplarda reklam yayımı edər.")
	
@TG.on_message(
	filters.command("help")
	& filters.private
)
async def hel(client, message):
	await message.reply_text("**Qrup Admin Əmrləri:**\n🔮 İstifadə: /tag\n📃 Açıqlama: Qrupdakı hərkəsi tağ edər.\n\n🔮 İstifadə: /admin\n📃 Açıqlama: Qrupdakı bütün adminləri tağ edər.\n\n🔮 İstifadə: /cancel\n📃 Açıqlama: Qrupdakı tağ prosesini dayandırar.\n\n**Bot Sahib Əmri:**\n🔮 İstifadə: /reklam\n📃 Açıqlama: Qruplarda reklam yayımı edər.")
	
@TG.on_message(
	filters.command(["admin", "all"])
	& filters.private
)
async def priw(client, message):
	await message.reply_text("Hmm burada 2-miz olduğumuz üçün və 2-mizdə online olduğumuz üçün bu əmri qruplarda işlət!🤠")


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
			await message.reply_text(f"{message.from_user.mention} Tağ prosesini başlatdı! Hərkəsi tağ edirəm! ⚡️",
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
			await message.reply_text(f"{message.from_user.mention} Adminləri tağ etməyimi istədi⚡️\nAdminləri tağ edirəm!🥳",
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
				await message.reply_text("Aktiv bir all prosesi yoxdur😕")
				return

			DUR = True
			await message.reply_text(f"{message.from_user.mention} Tağ prosesini dayandırdı❌ \nTamam heçkəsi tağ etmirəm😒")	
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
		await message.reply_text("<b>Sən botun sudo istifadəçisi deyilsen.</b>")


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
