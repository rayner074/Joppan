from pyrogram import Client, filters
from pyrogram.types import emoji

MENTION = "[{}](tg://user?id={})"
text1="hi{} {} welcome to Group Chat"


group ="jangobotz"
@bot.on_message(filters.chat(group) &filters.new_chat_members)
async def welcome(bot, message):
    new_members = [u.mention for u in message.new_chat_members]

    TEXT2= text1.format(emoji.SPARKLES,",".join(new_members))
    await message.reply_text(TEXT2)
