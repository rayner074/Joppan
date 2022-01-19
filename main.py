
import random
import pyrogram 
from pyrogram import Client as JanGo, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


bot = Client(
  "JanGo Bot",
  api_id = 11980417,
  api_hash = "0c04d148edcc0fb5ee0ef2254f7c1bc6",
  bot_token = "5065608218:AAFPSnj4CpXpqVe1kMKPtCpziCbtyB7FQZ8",
  
  )
  
  

START_TEXT = "welcome brother"    
   
PICS = "https://telegra.ph/file/6b6fe92e0a33b30e45303.jpg"


button = [
         [ InlineKeyboardButton("help", callback_data="help"),
           InlineKeyboardButton("about", callback_data="about")
           ],[
           InlineKeyboardButton("close", callback_data="close")]
           ]
      


@JanGo.on_message(filters.command(["start"]) & filters.private)
def start(bot, message):
       text="START_TEXT"
       reply_markup=InlineKeyboardMarkup(button)
       message.replay(
       text=text,
       reply_markup=reply_markup,
       disable_web_page_preview=True)
       
  
bot.run()
