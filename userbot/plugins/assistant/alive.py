from userbot import bot
from NEXTRON import xbot, ID
import heroku3
from telethon import events
from userbot import StartTime
import time
import datetime
from . import *
from telethon import events, Button, custom
import re, os
from NEXTRON import PHOTO, xbot, BOT, VERSION
from userbot import bot
@xbot.on(events.NewMessage(pattern=("/alive")))
async def awake(event):
  MAJID = f"Hᴇʟʟᴏ !! Tʜɪs ɪs **{BOT}**\n\n"
  MAJID += "**Aʟʟ sʏsᴛᴇᴍs ᴡᴏʀᴋɪɴɢ ᴘʀᴏᴘᴇʀʟʏ...**\n\n"
  MAJID += f"**{BOT} Vᴇʀsɪᴏɴ** : `{VERSION}`\n\n"
  MAJID += f"**Usᴇʀ** : @{bot.me.username}\n\n"
  MAJID += "**Fᴜʟʟʏ ᴜᴘᴅᴀᴛᴇᴅ ʙᴏᴛ...**\n\n"
  MAJID += "**Tᴇʟᴇᴛʜᴏɴ** : `1.20`\n\n"
  MAJID += "~~ **Tʜᴀɴᴋs ғᴏʀ ᴄʜᴇᴄᴋɪɴɢ ᴍᴇ** !!"
  BUTTON = [[Button.url("Mᴀsᴛᴇʀ", f"https://t.me/{bot.me.username}"), Button.url(f"{BOT} Rᴇᴘᴏ", "https://github.com/majid-nex/nextron-bot")]]
  BUTTON += [[custom.Button.inline("Rᴇᴘᴏsɪᴛᴏʀɪᴇs »»", data="MAJID")]]
  await xbot.send_file(event.chat_id, PHOTO, caption=LEGENDX,  buttons=BUTTON)




@xbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"MAJID")))
async def callback_query_handler(event):
# inline by LEGENDX22 and PROBOY22 🔥
  MAJID = [[Button.url("Rᴇᴘᴏ", "https://github.com/majid-nex/nextron-bot")]]
  MAJID +=[[Button.url("Dᴇᴘʟᴏʏ", "https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2FULTRA-OP%2FHEROKU&template=https%3A%2F%2Fgithub.com%2FULTRA-OP%2FHEROKU")]]
  MAJID +=[[Button.url("Tᴜᴛᴏʀɪᴀʟ", "https://youtu.be/rGCSSFPsS4Q"), Button.url("Sᴛʀɪɴɢ Sᴇssɪᴏɴ", "https://replit.com/@legendx22/ULTRA-X#main.py")]]
  MAJID +=[[Button.url("Aᴘɪ Iᴅ & Aᴘɪ Hᴀsʜ", "https://t.me/usetgxbot"), Button.url("Rᴇᴅɪs", "https://redislabs.com")]]
  MAJID +=[[Button.url("Sᴜᴘᴘᴏʀᴛ Cʜᴀɴɴᴇʟ", "https://t.me/ZEROTWOSUPPORT"), Button.url("Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ", "https://t.me/zerotwosupport")]]
  MAJID +=[[custom.Button.inline("«« Aʟɪᴠᴇ", data="MAJID")]]
  await event.edit(text=f"Aʟʟ Dᴇᴛᴀɪʟs Oғ Rᴇᴘᴏs", buttons=MAJID)


@xbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"MAJID")))
async def callback_query_handler(event):
# inline by LEGENDX22 and PROBOY22 🔥
  MAJID = f"Hᴇʟʟᴏ !! Tʜɪs ɪs **{BOT}**\n\n"
  MAJID += "**Aʟʟ sʏsᴛᴇᴍs ᴡᴏʀᴋɪɴɢ ᴘʀᴏᴘᴇʀʟʏ...**\n\n"
  MAJID += f"**{BOT} Vᴇʀsɪᴏɴ** : `{VERSION}`\n\n"
  MAJID += f"**Usᴇʀ** : @{bot.me.username}\n\n"
  MAJID += "**Fᴜʟʟʏ ᴜᴘᴅᴀᴛᴇᴅ ʙᴏᴛ...**\n\n"
  MAJID += "**Tᴇʟᴇᴛʜᴏɴ** : `1.20`\n\n"
  MAJID += "~~ **Tʜᴀɴᴋs ғᴏʀ ᴄʜᴇᴄᴋɪɴɢ ᴍᴇ** !!"
  BUTTONS = [[Button.url("Mᴀsᴛᴇʀ", f"https://t.me/{bot.me.username}"), Button.url(f"{BOT} Rᴇᴘᴏ", "https://github.com/majid-nex/nextron-bot")]]
  BUTTONS += [[custom.Button.inline("Rᴇᴘᴏsɪᴛᴏʀɪᴇs »»", data="MAJID")]]
  await event.edit(text=MAJID, buttons=BUTTONS)


@xbot.on(events.NewMessage(pattern=("/repo")))
async def repo(event):
  await xbot.send_message(event.chat, "**Hᴇʀᴇ Is Tʜᴇ Rᴇᴘᴏ Fᴏʀ NEXTRON Usᴇʀʙᴏᴛ** \n\nFᴏʀ Aɴʏ Hᴇʟᴘ :- @ZEROTWOSUPPORT", buttons=[[Button.url("⚜️ Rᴇᴘᴏ ⚜️", "https://github.com/majid-nex/nextron-bot"), Button.url("🔰 Dᴇᴘʟᴏʏ 🔰", "https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2FULTRA-OP%2FHEROKU&template=https%3A%2F%2Fgithub.com%2FULTRA-OP%2FHEROKU")]])


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time

@xbot.on(events.NewMessage(pattern=None))
async def ok(event):
    msg = str(event.text)
    if not msg == "/ping":
     return

    start_time = datetime.datetime.now()
    message = await event.reply("_.._.._Pinging_.._.._")
    end_time = datetime.datetime.now()
    pingtime = end_time - start_time
    telegram_ping = str(round(pingtime.total_seconds(), 2)) + "s"
    uptime = get_readable_time((time.time() - StartTime))
    await message.edit(
        "<b><i>☞ Pᴏɴɢ !!</i></b>\n"
        "<b>➥ Tɪᴍᴇ Tᴀᴋᴇɴ:</b> <code>{}</code>\n"
        "<b>➥ Sᴇʀᴠɪᴄᴇ Uᴘᴛɪᴍᴇ:</b> <code>{}</code>".format(telegram_ping, uptime),
        parse_mode="html",
    )
