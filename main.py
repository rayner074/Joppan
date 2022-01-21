from pyrogram import Client,filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
import asyncio
from info import Jk

bot = Client(
    "my first projrct",
    api_id=502966,
    api_hash="ba91c94ee88658b8702befa528544df3",
    bot_token="5065608218:AAGqoRYcy6wZfczCvYiXtIZUCNt4MLzIXyI",
    plugins = {"root": "bot" },
    sleep_threshold=5
)

 

@bot.on_message(filters.command("start") & filters.private)
def start(bot, message):
    button1 = [[
    InlineKeyboardButton("⚠️help", callback_data="help"),
    InlineKeyboardButton("🧳about", callback_data="about"),
    ],[
    InlineKeyboardButton("🚮 Close", callback_data="close")
    ]]
    text = Jk.START_TXT
    reply_markup = InlineKeyboardMarkup(button1)
    bot.send_photo(message.chat.id, Jk.PICS,
    caption=text,
    reply_markup=reply_markup,
    
    )
        
    
@bot.on_message(filters.command("help"))
def help(bot, message):
    button2 = [[
          InlineKeyboardButton("🦵Kick", callback_data="kick"),
          InlineKeyboardButton("👋Ban", callback_data="ban")
          ],[
          InlineKeyboardButton("🤫Mute", callback_data="mute"),
          InlineKeyboardButton("😌Unmute", callback_data="unmute")
          ],[
          InlineKeyboardButton("🤹about", callback_data="about"),
          InlineKeyboardButton("🗼home", callback_data="home")
          ],[
          InlineKeyboardButton("🚮 Close", callback_data="close")
          ]]
    reply_markup = InlineKeyboardMarkup(button2)
    bot.send_photo(message.chat.id, Jk.PICS,
    caption=Jk.START_TXT,
    reply_markup=reply_markup
    )
    

@bot.on_message(filters.command("photo"))
def photo(bot, message):
    bot.send_photo(message.chat.id, Jk.PICS,)

@bot.on_message(filters.command("alive"))
def alive(bot, message):
    buttonw = [[
    InlineKeyboardButton("⚠️help", callback_data="help"),
    InlineKeyboardButton("🧳about", callback_data="about")
    ],[
    InlineKeyboardButton("🎓home", callback_data="home")
    ],[
    InlineKeyboardButton("🚮 Close", callback_data="close")
    ]]

    bot.send_photo(message.chat.id, Jk.PICS,
    caption=Jk.START_TXT,
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
          ],[
          InlineKeyboardButton("🚮 Close", callback_data="close")
          ]]
        await query.message.edit_text(Jk.START_TEXT, reply_markup=InlineKeyboardMarkup(button))


    elif query.data == "help":
       button2 = [[
          InlineKeyboardButton("🦵Kick", callback_data="kick"),
          InlineKeyboardButton("👋Ban", callback_data="ban")
          ],[
          InlineKeyboardButton("🤫Mute", callback_data="mute"),
          InlineKeyboardButton("😌Unmute", callback_data="unmute")
          ],[
          InlineKeyboardButton("🤹about", callback_data="about"),
          InlineKeyboardButton("🗼home", callback_data="home")
          ],[
          InlineKeyboardButton("🚮 Close", callback_data="close")
          ]]
   
       await query.message.edit_text(Jk.HELP_TXT,reply_markup=InlineKeyboardMarkup(button))


    elif query.data == "about":
        button = [[
          InlineKeyboardButton("⚠️help", callback_data="help"),
          ],[
          InlineKeyboardButton("🎓home", callback_data="home")
          ],[
          InlineKeyboardButton("🚮 Close", callback_data="close")
          ]]
        await query.message.edit_text(Jk.ABOUT_TXT,reply_markup=InlineKeyboardMarkup(button))

    elif query.data == "home":
        button = [[
          InlineKeyboardButton("⚠️help", callback_data="help"),
          ],[
          InlineKeyboardButton("About", callback_data="about")
          ],[
          InlineKeyboardButton("🚮 Close", callback_data="close")
          ]]
        await query.message.edit_text(Jk.START_TXT,reply_markup=InlineKeyboardMarkup(button))
     elif query.data == "kick":
        button = [[
          InlineKeyboardButton("⬅️Back", callback_data="help"),
          ]] 
        await query.message.edit_text(Jk.KICK_TXT,reply_markup=InlineKeyboardMarkup(button))
     
     elif query.data == "ban":
        button = [[
          InlineKeyboardButton("⬅️Back", callback_data="help"),
          ]] 
        await query.message.edit_text(Jk.BAN_TXT,reply_markup=InlineKeyboardMarkup(button)) 
     elif query.data == "mute":
        button = [[
          InlineKeyboardButton("⬅️Back", callback_data="help"),
          ]] 
        await query.message.edit_text(Jk.MUTE_TXT,reply_markup=InlineKeyboardMarkup(button))
     elif query.data == "unmute":
        button = [[
          InlineKeyboardButton("⬅️Back", callback_data="help"),
          ]] 
        await query.message.edit_text(Jk.KICK_TXT,reply_markup=InlineKeyboardMarkup(button))


bot.run()
