import asyncio
import os
try:
  from pyrogram import Client, idle
except:
  os.system("pip install pyrogram>=1.1.13")
  from pyrogram import Client, idle

import asyncio
from userbot.utils import admin_cmd as majid
from userbot import bot as Nextron
API_ID = os.environ.get("APP_ID", None)
API_HASH = os.environ.get("API_HASH", None)
from telethon import events, custom, Button, TelegramClient
import time
from userbot import botnickname, ALIVE_NAME, bot
token = os.environ.get("TG_BOT_TOKEN_BF_HER", None)
xbot = TelegramClient("legend", API_ID, API_HASH).start(bot_token=token)
pbot = Client("NEX", api_id=API_ID, api_hash=API_HASH, bot_token=token)
BOT = str(botnickname) if botnickname else "NEXTRON BOT"
NAME = str(ALIVE_NAME) if ALIVE_NAME else "NEX BOY"
PHOTO = os.environ.get("ALIVE_PHOTTO", None)
MAJID = "[MAJID](https://t.me/Mr_Godfather9)"
VERSION = "1.1.1"
REPO = "[NEXTRON](https://github.com/majid-nex/nextron-bot)"
PRO = bot.uid
MASTER = f"[{NAME}](tg://user?id={PRO})"
GROUP = "[SUPPORT GROUP](https://t.me/NEXTRONSUPPORT)"
if __name__=="__main__":
  xbot.run_until_disconnected()

if __name__=="__main__":
  pbot.start()
