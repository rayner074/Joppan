from pyrogram import Client as bot, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
import asyncio
from info import Jk

@bot.on_message(filters.command("start") & filters.private)
def start(bot, message):
    button1 = [[
    InlineKeyboardButton("â ï¸ Help", callback_data="help"),
    InlineKeyboardButton("ð¡ï¸ About", callback_data="about"),
    ],[
    InlineKeyboardButton("ð® Close", callback_data="close")
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
          InlineKeyboardButton("ð¦µ Kick", callback_data="kick"),
          InlineKeyboardButton("ð Ban", callback_data="ban")
          ],[
          InlineKeyboardButton("ð¤« Mute", callback_data="mute"),
          InlineKeyboardButton("ð Unmute", callback_data="unmute"),
          InlineKeyboardButton("ðï¸ User Info", callback_data="usrinfo")
          ],[
          InlineKeyboardButton("ð¡ï¸ about", callback_data="about"),
          InlineKeyboardButton("ð¼ home", callback_data="home")
          ],[
          InlineKeyboardButton("ð® Close", callback_data="close"),
          InlineKeyboardButton("â¬ï¸Back", callback_data="start")
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
    InlineKeyboardButton("â ï¸ Help", callback_data="help"),
    InlineKeyboardButton("ð¡ï¸ About", callback_data="about")
    ],[
    InlineKeyboardButton("ð¼ Home", callback_data="home")
    ],[
    InlineKeyboardButton("ð® Close", callback_data="close")
    ]]

    bot.send_photo(message.chat.id, Jk.PICS,
    caption=Jk.START_TXT,
    reply_markup=InlineKeyboardMarkup(buttonw)
    )
