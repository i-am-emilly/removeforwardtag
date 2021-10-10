import re, os, random, asyncio, html
os.system("pip install --upgrade pip")
os.system("pip install pyrogram")
import pyrogram
from pyrogram.errors import RPCError
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

APP_ID = os.environ.get("APP_ID")
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")

app = pyrogram.Client("app", api_id=APP_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

botmaker = InlineKeyboardMarkup([[InlineKeyboardButton("Help 🤔", callback_data="Help"), InlineKeyboardButton("Close 🔐", callback_data="close")],[InlineKeyboardButton("owner ⬆", url="t.me/adarshgoelo5"), InlineKeyboardButton("Developer 💕", url="t.me/adarshgoelo5")]])
adarsh = InlineKeyboardMarkup([[InlineKeyboardButton("Home 🏠", callback_data="home"), InlineKeyboardButton("contact owner⬆",url="t.me/adarshgoelo5")], [InlineKeyboardButton("Repo 👉", url="https://github.com/adarsh-goel/removeforwardtag"), InlineKeyboardButton("Close 🔐", callback_data="close")]])


@app.on_message(filters.command(["start"]))
async def start(lel, message):
    await message.reply_text(f"**Hi** `{message.from_user.first_name}` **!\n\nI'm Channel,Group and Private chat forward tag remover! I can send the file // messages which is forwarded in the chat where I amadded without forward tag.🤩..!**", reply_markup=botmaker)

@app.on_message(filters.command(["help"]))
async def help(ha, message):
    await app.send_message(message.chat.id, """**There is nothing here ..!\nSend me forwarded message//file or Just add me to your channel//group and  give rights to delete message and post messages and whenever I will recieve a forwarded message  I will send again without forward tag.\n\nMade with ❤️ by @adarshgoelo5**""", reply_markup=adarsh) 

@app.on_callback_query()
async def button(app, update):
    k = update.data
    if "Help" in k:
       await update.message.delete()
       await help(app, update.message)
    elif "close" in k:
       await update.message.delete()
    elif "home" in k:
       await update.message.delete()
       await start(app, update.message)

@app.on_message(filters.channel & filters.forwarded)
async def copy(sed, message):
    try:
       
       sed = await message.copy(message.chat.id)
       
       await message.delete()
    except RPCError as lel:
       await message.reply(lel)
       return
    
@app.on_message(filters.group & filters.forwarded)
async def copy(sed, message):
    try:
       
       sed = await message.copy(message.chat.id)
       
       await message.delete()
    except RPCError as lel:
       await message.reply(lel)
       return
 
@app.on_message(filters.private & filters.forwarded)
async def copy(sed, message):
    try:
       
       sed = await message.copy(message.chat.id)
       
       await message.delete()
    except RPCError as lel:
       await message.reply(lel)
       return


print("Started bot...! ") 
print("contact @adarshgoelo5 for any help !")
app.run()
