
from info import API_ID, API_HASH, BOT_TOKEN
from pyrogram import Client, __version__
from pyrogram.raw.all import layer 

bot = Client (
  "JanGo Bot",
  api_id = API_ID,
  api_hash = API_HASH,
  bot_token = BOT_TOKEN
  plugins={
                "root": "commands"
            },
  )
  
  Print("alive")

bot.run()
