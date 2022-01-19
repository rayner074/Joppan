from . import Commands
import pyrogram
from pyrogram import Client, filters

bot = Client (
  "JanGo Bot",
  api_id = 11980417,
  api_hash = "0c04d148edcc0fb5ee0ef2254f7c1bc6",
  bot_token = "5040881620:AAF8bvIFscFDf2Dro9CHI78-U6T4S20ieQI"
  )
  
print("alive")
  
bot.run()
