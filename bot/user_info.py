from pyrogram import Client as bot, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
import asyncio
from info import Jk

@bot.on_message(filters.command('id'))
async def showid(client, message): 
    chat_type = message.chat.type 
    if chat_type == "private":
        user_id = message.chat.id 
        first = message.from_user.first_name 
        last = message.from_user.last_name or "" 
        username = message.from_user.username 
        
        buttons = [[
            InlineKeyboardButton('🚮 Close', callback_data='close')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        text=f"<b>♟️First Name:</b> {first}\n<b>🎯Last Name:</b> {last}\n<b>🎗️Username:</b> {username}\n<b>🎰Telegram ID:</b> <code>{user_id}</code>\n"
        await message.reply_text(
        text=text, 
        reply_markup=reply_markup
        )

    elif chat_type in ["group", "supergroup"]:
        user_id = message.from_user.id
        chat_id = message.chat.id
        if message.reply_to_message:
            reply_id = f"<b>🎯 Replied User ID:</b> `{message.reply_to_message.from_user.id}`"
        else:
            reply_id = ""
            
        await message.reply_text(
            f"<b>📌 Your ID:<\b> `{user_id}`\n<b>🎗️This Group ID:<b/> `{chat_id}`\n{reply_id}",
            parse_mode="md",
            quote=True
        )          


@bot.on_message(filters.command('info'))
async def showinfo(client, message): 
    chat_type = message.chat.type 
    if chat_type == "private":
        user_id = message.chat.id 
        first = message.from_user.first_name 
        last = message.from_user.last_name or "None" 
        username = message.from_user.username 
        buttons = [[
            InlineKeyboardButton('🚮 Close', callback_data='close')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)  
        text1=f"<b>♟️First Name:</b> {first}\n<b>🎯Last Name:</b> {last}\n<b>🎗️Username:</b> @{username}\n<b>🎰Telegram ID:</b> <code>{user_id}</code>\n<b>♻️User Link:</b> <a href='tg://user?id={user_id}'><b>Click Here</b></a>\n" 
        await message.reply_text(
        text=text1, 
        reply_markup=reply_markup
        )
