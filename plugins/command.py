#python 3.7.1

import random
import pyrogram 
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

JanGo = Client("JanGo Bot")

@JanGo.on_message(filters.command(["start"]) & filters.private, group=1)
async def start(bot, message):
     bot.send_message(message.chat_id, "START_TEXT")
        button = [[
           InlineKeyboardButton("help", callback_data="help"),
           InlineKeyboardButton("about", callback_data="about")
           ],[
           InlineKeyboardButton("close", callback_data="close")
           ]]
       reply_markup = InlineKeyboardMarkup(buttons)



START_TEXT = """
welcome brother
 """       
PICS = "https://telegra.ph/file/6b6fe92e0a33b30e45303.jpg"
