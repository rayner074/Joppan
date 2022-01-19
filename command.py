#python 3.7.1

import random
import pyrogram 
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

JanGo = Client("JanGo Bot")

@JanGo.on_message(filters.command(["start"]) & filters.private, group=1)
async def start(bot, message):
        button = [[
           InlineKeyboardButton("help", callback_data="help")
           InlineKeyboardButton("about", callback_data="about")
           ],[
           InlineKeyboardButton("close", callback_data="close")"
           ]
           await bot.send_photo(
            chat_id=message.chat.id,
            photo=random.choice(PICS),
            caption=START_TEXT,
            reply_markup = InlineKeyboardMarkup(button),
            parse_mode="html", 
            reply_to_message_id=message.message_id
        )



  START_TEXT = """
  Welcome brother
 """       
  PICS = "https://telegra.ph/file/6b6fe92e0a33b30e45303.jpg"