from pyrogram import Client,filters

bot = Client(
    "my first projrct",
    api_id=502966,
    api_hash="ba91c94ee88658b8702befa528544df3",
    bot_token="5065608218:AAFPSnj4CpXpqVe1kMKPtCpziCbtyB7FQZ8"
)
@bot.on_message(filters.command("start") & filters.private)
def start(bot, message):
    bot.send_message(message.chat.id,"hey bro")

bot.run()
