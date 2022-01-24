from pyrogram import Client as bot, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
import asyncio
from info import Jk

from database.connections_mdb import(
    all_connections,
    active_connection,
    if_active,
    delete_connection,
    make_active,
    make_inactive
)

@bot.on_callback_query()
async def cb_handler(bot, query):

    if query.data == "close":
        await query.message.delete()

    elif query.data == "start":
        button = [[     
          InlineKeyboardButton("⚠️ 𝖧𝖾𝗅𝗉", callback_data="help"),
          InlineKeyboardButton("🛡️ 𝖠𝖻𝗈𝗎𝗍", callback_data="about")
          ],[
          InlineKeyboardButton("🚮 Close", callback_data="close")
          ]]
        await query.message.edit_text(Jk.START_TXT, reply_markup=InlineKeyboardMarkup(button))


    elif query.data == "help":
       button = [[
          InlineKeyboardButton("🦵 Kick", callback_data="kick"),
          InlineKeyboardButton("👋 Ban", callback_data="ban")
          ],[
          InlineKeyboardButton("🤫 Mute", callback_data="mute"),
          InlineKeyboardButton("😌 Unmute", callback_data="unmute"),
          InlineKeyboardButton("🎗️ User Info", callback_data="usrinfo")
          ],[
          InlineKeyboardButton("🛡️ About", callback_data="about"),
          InlineKeyboardButton("🗼 Home", callback_data="home")
          ],[
          InlineKeyboardButton("🚮 Close", callback_data="close"),
          InlineKeyboardButton("⬅️ Back", callback_data="start")
          ]]
   
       await query.message.edit_text(Jk.HELP_TXT,reply_markup=InlineKeyboardMarkup(button))


    elif query.data == "about":
       button = [[
          InlineKeyboardButton("⚠️ help", callback_data="help"),
          InlineKeyboardButton("🗼 Home", callback_data="home")
          ],[
          InlineKeyboardButton("🚮 Close", callback_data="close"),
          InlineKeyboardButton("⬅️Back", callback_data="help")
          ]]
       await query.message.edit_text(Jk.ABOUT_TXT,reply_markup=InlineKeyboardMarkup(button))

    elif query.data == "home":
       button = [[
          InlineKeyboardButton("⚠️ Help", callback_data="help"),
          InlineKeyboardButton("🛡️ About", callback_data="about")
          ],[
          InlineKeyboardButton("🚮 Close", callback_data="close")
          ]]
       await query.message.edit_text(Jk.START_TXT,reply_markup=InlineKeyboardMarkup(button))
    elif query.data == "kick":
       button = [[
          InlineKeyboardButton("⬅️Back", callback_data="help")
          ]] 
       await query.message.edit_text(Jk.KICK_TXT,reply_markup=InlineKeyboardMarkup(button))
     
    elif query.data == "ban":
       button = [[
          InlineKeyboardButton("⬅️Back", callback_data="help")
          ]] 
       await query.message.edit_text(Jk.BAN_TXT,reply_markup=InlineKeyboardMarkup(button)) 
    elif query.data == "mute":
       button = [[
          InlineKeyboardButton("⬅️Back", callback_data="help")
          ]] 
       await query.message.edit_text(Jk.MUTE_TXT,reply_markup=InlineKeyboardMarkup(button))
    elif query.data == "unmute":
       button = [[
          InlineKeyboardButton("⬅️Back", callback_data="help")
          ]] 
       await query.message.edit_text(Jk.UNMUTE_TXT,reply_markup=InlineKeyboardMarkup(button))

    elif query.data == "usrinfo":
       button = [[
          InlineKeyboardButton("⬅️Back", callback_data="help")
          ]] 
       await query.message.edit_text(Jk.USERINFO_TXT,reply_markup=InlineKeyboardMarkup(button))

    elif query.data == "delallconfirm":
        userid = query.from_user.id
        chat_type = query.message.chat.type

        if chat_type == "private":
            grpid  = await active_connection(str(userid))
            if grpid is not None:
                grp_id = grpid
                try:
                    chat = await client.get_chat(grpid)
                    title = chat.title
                except:
                    await query.message.edit_text("Make sure I'm present in your group!!", quote=True)
                    return
            else:
                await query.message.edit_text(
                    "I'm not connected to any groups!\nCheck /connections or connect to any groups",
                    quote=True
                )
                return

        elif (chat_type == "group") or (chat_type == "supergroup"):
            grp_id = query.message.chat.id
            title = query.message.chat.title

        else:
            return

        st = await client.get_chat_member(grp_id, userid)
        if (st.status == "creator"):    
            await del_all(query.message, grp_id, title)
        else:
            await query.answer("You need to be Group Owner or an Auth User to do that!",show_alert=True)
    
    elif query.data == "delallcancel":
        userid = query.from_user.id
        chat_type = query.message.chat.type
        
        if chat_type == "private":
            await query.message.reply_to_message.delete()
            await query.message.delete()

        elif (chat_type == "group") or (chat_type == "supergroup"):
            grp_id = query.message.chat.id
            st = await client.get_chat_member(grp_id, userid)
            if (st.status == "creator"):
                await query.message.delete()
                try:
                    await query.message.reply_to_message.delete()
                except:
                    pass
            else:
                await query.answer("Thats not for you!!",show_alert=True)


    elif "groupcb" in query.data:
        await query.answer()

        group_id = query.data.split(":")[1]
        title = query.data.split(":")[2]
        act = query.data.split(":")[3]
        user_id = query.from_user.id

        if act == "":
            stat = "CONNECT"
            cb = "connectcb"
        else:
            stat = "DISCONNECT"
            cb = "disconnect"

        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton(f"{stat}", callback_data=f"{cb}:{group_id}:{title}"),
                InlineKeyboardButton("DELETE", callback_data=f"deletecb:{group_id}")],
            [InlineKeyboardButton("BACK", callback_data="backcb")]
        ])

        await query.message.edit_text(
            f"Group Name : **{title}**\nGroup ID : `{group_id}`",
            reply_markup=keyboard,
            parse_mode="md"
        )
        return

    elif "connectcb" in query.data:
        await query.answer()

        group_id = query.data.split(":")[1]
        title = query.data.split(":")[2]
        user_id = query.from_user.id

        mkact = await make_active(str(user_id), str(group_id))

        if mkact:
            await query.message.edit_text(
                f"Connected to **{title}**",
                parse_mode="md"
            )
            return
        else:
            await query.message.edit_text(
                f"Some error occured!!",
                parse_mode="md"
            )
            return

    elif "disconnect" in query.data:
        await query.answer()

        title = query.data.split(":")[2]
        user_id = query.from_user.id

        mkinact = await make_inactive(str(user_id))

        if mkinact:
            await query.message.edit_text(
                f"Disconnected from **{title}**",
                parse_mode="md"
            )
            return
        else:
            await query.message.edit_text(
                f"Some error occured!!",
                parse_mode="md"
            )
            return
    elif "deletecb" in query.data:
        await query.answer()

        user_id = query.from_user.id
        group_id = query.data.split(":")[1]

        delcon = await delete_connection(str(user_id), str(group_id))

        if delcon:
            await query.message.edit_text(
                "Successfully deleted connection"
            )
            return
        else:
            await query.message.edit_text(
                f"Some error occured!!",
                parse_mode="md"
            )
            return
    
    elif query.data == "backcb":
        await query.answer()

        userid = query.from_user.id

        groupids = await all_connections(str(userid))
        if groupids is None:
            await query.message.edit_text(
                "There are no active connections!! Connect to some groups first.",
            )
            return
        buttons = []
        for groupid in groupids:
            try:
                ttl = await client.get_chat(int(groupid))
                title = ttl.title
                active = await if_active(str(userid), str(groupid))
                if active:
                    act = " - ACTIVE"
                else:
                    act = ""
                buttons.append(
                    [
                        InlineKeyboardButton(
                            text=f"{title}{act}", callback_data=f"groupcb:{groupid}:{title}:{act}"
                        )
                    ]
                )
            except:
                pass
        if buttons:
            await query.message.edit_text(
                "Your connected group details ;\n\n",
                reply_markup=InlineKeyboardMarkup(buttons)
            )

    elif "alertmessage" in query.data:
        grp_id = query.message.chat.id
        i = query.data.split(":")[1]
        keyword = query.data.split(":")[2]
        reply_text, btn, alerts, fileid = await find_filter(grp_id, keyword)
        if alerts is not None:
            alerts = ast.literal_eval(alerts)
            alert = alerts[int(i)]
            alert = alert.replace("\\n", "\n").replace("\\t", "\t")
            await query.answer(alert,show_alert=True)
