# updated by majid
from telethon import events, Button, custom
from userbot import bot
from NEXTRON import xbot
# updated by majid
import os,re
from telethon.tl.custom import Button 
from telethon import events, errors, custom, functions
@xbot.on(events.InlineQuery(pattern=r"repo"))
async def inline_id_handler(event: events.InlineQuery.Event):
 # updated by majid
 NEXTRON = event.builder
 X= [[custom.Button.inline("🔥 Cʟɪᴄᴋ Hᴇʀᴇ 🔥",data="obhai")]]
 query = event.text
 # updated by majid
 result = NEXTRON.article("Nextron",text="**Nextron Rᴇᴘᴏ, Dᴇᴘʟᴏʏ ᴀɴᴅ Sᴜᴘᴘᴏʀᴛ\n\n© @ZEROTWOSUPPORT**",buttons=X,link_preview=False)
 # updated by majid
 await event.answer([result])
@xbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"obhai")))
# updated by majid
async def callback_query_handler(event):
# inline by TEAMNextron, Majid
  await event.edit(text=f"**Nextron's Rᴇᴘᴏ, Dᴇᴘʟᴏʏ ᴀɴᴅ Gʀᴏᴜᴘ Lɪɴᴋ\n\n© @ZEROTWOSUPPORT**",buttons=[
   # updated by majid
                [
                    Button.url(f"⚜️ Rᴇᴘᴏ ⚜️", url="https://github.com/MAJID-NEX/NEXTRON-BOT"),
                 # updated by majdi
                    Button.url(f"🌚 Sᴜᴘᴘᴏʀᴛ Cʜᴀᴛ 🌝", url="https://t.me/ZEROTWOSUPPORT")],
                    [Button.url(f"🔰 Dᴇᴘʟᴏʏ 🔰", url="https://heroku.com/deploy?template=https://github.com/majid-nex/NEXTRONBOT.git"),
                     Button.url(f"💠 Sᴛʀɪɴɢ 💠", url="https://replit.com/majidyt/NEXTRONBOT#main.py"),
                ]
            ]
                  )
