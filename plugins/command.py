#python 3.7.1

import random
import pyrogram 
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

JanGo = Client("JanGo Bot")

START_TEXT = "welcome brother"    
   
PICS = "https://telegra.ph/file/6b6fe92e0a33b30e45303.jpg"


button = [
         [ InlineKeyboardButton("help", callback_data="help"),
           InlineKeyboardButton("about", callback_data="about")
           ],[
           InlineKeyboardButton("close", callback_data="close")]
           ]
      


@JanGo.on_message(filters.command(["start"]) & filters.private, group=1)
    def start(bot, message):
       text = START_TEXT
       reply_markup = InlineKeyboardMarkup(button)
       message.replay(
       text=text,
       reply_markup = reply_markup,
       disable_web_page_preview = True



