
from info import API_ID, API_HASH, BOT_TOKEN
import pyrogram
from pyrogram import Client

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
