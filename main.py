
from info import API_ID, API_HASH, BOT_TOKEN
import pyrogram
from pyrogram import Client

JanGo = Client (
  "JanGo Bot",
  api_id = API_ID,
  api_hash = API_HASH,
  bot_token = BOT_TOKEN
  )
  
  app = JanGo,
  app.run()
