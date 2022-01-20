from pyrogram import Client,filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
import asyncio

bot = Client(
    "my first projrct",
    api_id=502966,
    api_hash="ba91c94ee88658b8702befa528544df3",
    bot_token="5065608218:AAFPSnj4CpXpqVe1kMKPtCpziCbtyB7FQZ8"
)

START_TXT = "hey bro welcome"
HELP_TXT =" help section"
ABOUT_TXT ="about section"
 

@bot.on_message(filters.command("start") & filters.private)
def start(bot, message):
    button1 = [[
    InlineKeyboardButton("⚠️help", callback_data="help"),
    InlineKeyboardButton("🧳about", callback_data="about")
    ]]
    text = START_TXT
    reply_markup = InlineKeyboardMarkup(button1)
    bot.send_photo(message.chat.id, "https://telegra.ph/file/67fee801475d5bd21549a.jpg",
    caption=text,
    reply_markup=reply_markup,
    
    )
        
    
@bot.on_message(filters.command("help"))
def help(bot, message):
    button2 = [[
          InlineKeyboardButton("🧳about", callback_data="about")],[
          InlineKeyboardButton("🎓home", callback_data="home")
          ]]
    reply_markup = InlineKeyboardMarkup(button2)
    bot.send_photo(message.chat.id, "https://telegra.ph/file/67fee801475d5bd21549a.jpg",
    caption=START_TXT,
    reply_markup=reply_markup
    )
    

@bot.on_message(filters.command("photo"))
def photo(bot, message):
    bot.send_photo(message.chat.id, "https://telegra.ph/file/67fee801475d5bd21549a.jpg")

@bot.on_message(filters.command("alive"))
def alive(bot, message):
    buttonw = [[
    InlineKeyboardButton("⚠️help", callback_data="help"),
    InlineKeyboardButton("🧳about", callback_data="about")
    ],[
    InlineKeyboardButton("🎓home", callback_data="home")
    ]]

    bot.send_photo(message.chat.id, "https://telegra.ph/file/67fee801475d5bd21549a.jpg",
    caption=START_TXT,
    reply_markup=InlineKeyboardMarkup(buttonw)
    )
@bot.on_callback_query()
async def cb_handler(bot, query):

    if query.data == "close":
        await query.message.delete()

    elif query.data == "start":
        button = [[  
          
          InlineKeyboardButton("⚠️ 𝖧𝖾𝗅𝗉", callback_data="help"),
          InlineKeyboardButton("𝖠𝖻𝗈𝗎𝗍 🤠", callback_data="about")
          ]]
        await query.message.edit_text(START_TEXT, reply_markup=InlineKeyboardMarkup(button))


    elif query.data == "help":
       button = [[
          InlineKeyboardButton("🧳about", callback_data="about")],[
          InlineKeyboardButton("🎓home", callback_data="home")
          ]]
       await query.message.edit_text(HELP_TXT,reply_markup=InlineKeyboardButton(button))


    elif query.data == "about":
        button = [[
          InlineKeyboardButton("⚠️help", callback_data="help"),
          ],[
          InlineKeyboardButton("🎓home", callback_data="home")
          ]]
        await query.message.edit_text(ABOUT_TXT,reply_markup=InlineKeyboardButton(button))


bot.run()
