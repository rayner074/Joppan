#python 3.7.1

import random
import pyrogram 
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

JanGo = Client("JanGo Bot")

button = [[
           InlineKeyboardButton("help", callback_data="help"),
           InlineKeyboardButton("about", callback_data="about")
           ],[
           InlineKeyboardButton("close", callback_data="close")
           ]]
      reply_markup = InlineKeyboardMarkup(button)


@JanGo.on_message(filters.command(["start"]) & filters.private, group=1)
async def start(bot, message):
       bot.send_photo("me", "https://telegra.ph/file/6b6fe92e0a33b30e45303.jpg", caption="Holidays!")  


START_TEXT = """
welcome brother
 """       
PICS = "https://telegra.ph/file/6b6fe92e0a33b30e45303.jpg"
