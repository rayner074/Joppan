from pyrogram import Client,filters
import asyncio
from info import Jk

bot = Client(
    "my first projrct",
    api_id=502966,
    api_hash="ba91c94ee88658b8702befa528544df3",
    bot_token="5153914057:AAFRXIrS5QYHZT2guNVZkSdkKbpIofkYgVY",
    plugins = {"root": "bot" },
    sleep_threshold=5
)

 


bot.run()
