import asyncio
import os
try:
  from pyrogram import Client, idle
except:
  os.system("pip install pyrogram>=1.1.13")
  from pyrogram import Client, idle

import asyncio
from userbot import bot as GODBOYX
API_ID = os.environ.get("APP_ID", None)
API_HASH = os.environ.get("API_HASH", None)
from telethon import events, custom, Button, TelegramClient
import time
from userbot import botnickname, ALIVE_NAME, bot
token = os.environ.get("TG_BOT_TOKEN_BF_HER", None)
xbot = TelegramClient("Nextron", API_ID, API_HASH).start(bot_token=token)
pbot = Client("Nextron", api_id=API_ID, api_hash=API_HASH, bot_token=token)
BOT = str(botnickname) if botnickname else "Nextron bot"
NAME = str(ALIVE_NAME) if ALIVE_NAME else "Nextron user"
PHOTO = os.environ.get("ALIVE_PHOTO", None)
NEXTRON = "[Nextron](https://t.me/nextronsupport)"
VERSION = "1.1.0"
ID = 1742906647
REPO = "[Userbot](https://github.com/majid-nex/nextron-bot)"
devs = 1742906647
MASTER = f"[{NAME}](tg://user?id={ID})"
GROUP = "[SUPPORT GROUP](https://t.me/nextronSupport)"
if __name__=="__main__":
  xbot.run_until_disconnected()

if __name__=="__main__":
  pbot.start()
  run()
