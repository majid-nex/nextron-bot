import asyncio
import os
import requests
import time
from PIL import Image
from . import legend
from io import BytesIO
from datetime import datetime
import random
from telethon import events
from userbot.utils import admin_cmd, sudo_cmd
from userbot import ALIVE_NAME, StartTime
from telethon.tl.types import ChannelParticipantsAdmins
# 🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "NEXTRON SIR"
ALIVE_PHOTTO = os.environ.get("ALIVE_PHOTTO" , None)

global ghanti
ghanti = borg.uid
edit_time = 5
""" =======================CONSTANTS====================== """
file1 = "https://telegra.ph/file/a44f1363bddbba84a2b98.jpg"
file2 = "https://telegra.ph/file/b635b26bcb08c7fe705c9.jpg"
file3 = "https://telegra.ph/file/e027c90d03bae039ab58e.jpg"
file4 = "https://telegra.ph/file/21e8ba90ef8b22fa6a864.jpg"
""" =======================CONSTANTS====================== """
pm_caption = " NEXTRON IS ONLINE\n\n"
pm_caption += "Yes Master, Am Alive And Systems Are Working Perfectly As It Should Be...\n\n"
pm_caption += "✘ About My System ✘\n\n"
pm_caption += "➾ ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀꜱɪᴏɴ ☞ 1.18.2\n"
pm_caption += "➾ ꜱᴜᴘᴘᴏʀᴛ ᴄʜᴀɴɴᴇʟ ☞ [ᴊᴏɪɴ](https://t.me/nextronsupport)\n"
pm_caption += "➾ ʟɪᴄᴇɴꜱᴇ  ☞ [TEAM NEXTRON](https://github.com/majid-nex)\n"
pm_caption += "➾ group ☞ [NEXTRON TEAM](https://t.me/nextronsupport)\n\n"
pm_caption += f"➾ ᴍʏ ᴍᴀsᴛᴇʀ ☞ [{DEFAULTUSER}](tg://user?id={ghanti})\n"

@borg.on(admin_cmd(pattern=r"alive"))
@borg.on(sudo_cmd(pattern=r"alive", allow_sudo=True))

async def amireallyalive(yes):
    chat = await yes.get_chat()
    global ghanti
    ghanti = borg.uid
##
    on = await borg.send_file(yes.chat_id, file=file1,caption=pm_caption)

    await asyncio.sleep(edit_time)
    ok = await borg.edit_message(yes.chat_id, on, file=file2) 

    await asyncio.sleep(edit_time)
    ok2 = await borg.edit_message(yes.chat_id, ok, file=file3)

    await asyncio.sleep(edit_time)
    ok3 = await borg.edit_message(yes.chat_id, ok2, file=file1)
    
    await asyncio.sleep(edit_time)
    ok4 = await borg.edit_message(yes.chat_id, ok3, file=file3)
    
    await asyncio.sleep(edit_time)
    ok5 = await borg.edit_message(yes.chat_id, ok4, file=file2)
    
    await asyncio.sleep(edit_time)
    ok6 = await borg.edit_message(yes.chat_id, ok5, file=file1)
    
    await asyncio.sleep(edit_time)
    ok7 = await borg.edit_message(yes.chat_id, ok6, file=file4)

    await yes.delete()

""" For .alive command, check if the bot is running.  """
    
    

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


@borg.on(admin_cmd(outgoing=True, pattern="salive"))
@borg.on(sudo_cmd(pattern=r"salive", allow_sudo=True))
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    if ALIVE_PHOTTO:
        pm_caption = "Nextron 𝙸𝚂 🅾︎🅽🅻🅸🅽🅴\n"
        pm_caption += f"𝕄𝕪 𝔹𝕠𝕤𝕤            : {DEFAULTUSER}\n"
        pm_caption += "𝚃𝙴𝙻𝙴𝚃𝙷𝙾𝙽 𝚅𝙴𝚁𝚂𝙸𝙾𝙽        : 1.18.2\n"
        pm_caption += "𝙿𝚈𝚃𝙷𝙾𝙽 𝚅𝙴𝚁𝚂𝙸𝙾𝙽          : 3.9.0\n"
        pm_caption += "𝚂𝚄𝙿𝙿𝙾𝚁𝚃 𝙲𝙷𝙰𝙽𝙽𝙴𝙻         : [ᴊᴏɪɴ](https://t.me/nextronsupport)\n"
        pm_caption += "𝚂𝚄𝙿𝙿𝙾𝚁𝚃 𝙶𝚁𝙾𝚄𝙿           : [ᴊᴏɪɴ](https://t.me/nextronsupport)\n"
        pm_caption += "𝘾𝙊𝙋𝙔𝙍𝙄𝙂𝙃𝙏 𝘽𝙔            : [ Nextron](https://t.me/nextronsupport)\n"
        pm_caption += "[┏┓━┏┓━━━━┏┓━┏┓━━━━━\n ┃┃━┃┃━━━━┃┃━┃┃━━━━━\n ┃┗━┛┃┏━━┓┃┃━┃┃━┏━━┓\n ┃┏━┓┃┃┏┓┃┃┃━┃┃━┃┏┓┃ \n ┃┃━┃┃┃┃━┫┃┗┓┃┗┓┃┗┛┃ \n ┗┛━┗┛┗━━┛┗━┛┗━┛┗━━┛](https://t.me/Dark_cobra_support_group)"
        chat = await alive.get_chat()
        await alive.delete()
        """ For .allive command, check if the bot is running.  """
        await borg.send_file(alive.chat_id, ALIVE_PHOTTO,caption=pm_caption, link_preview = False)
        await allive.delete()
        return
    req = requests.get("https://telegra.ph/file/6d067b1a626a25735f5ed.png")
    req.raise_for_status()
    file = BytesIO(req.content)
    file.seek(0)
    img = Image.open(file)
    with BytesIO() as sticker:
        img.save(sticker, "webp")
        sticker.name = "sticker.webp"
        sticker.seek(0)
        await borg.send_file(alive.chat_id, file=sticker)
        await borg.send_message(alive.chat_id,"Nextron 𝙸𝚂 🅾︎🅽🅻🅸🅽🅴\n"
                      f"𝕄𝕪 𝔹𝕠𝕤𝕤            : {DEFAULTUSER}\n"
                      "𝚃𝙴𝙻𝙴𝚃𝙷𝙾𝙽 𝚅𝙴𝚁𝚂𝙸𝙾𝙽        : 1.18.2\n"
                      "𝙿𝚈𝚃𝙷𝙾𝙽 𝚅𝙴𝚁𝚂𝙸𝙾𝙽          : 3.9.0\n"
                      "𝚂𝚄𝙿𝙿𝙾𝚁𝚃 𝙲𝙷𝙰𝙽𝙽𝙴𝙻         : [ᴊᴏɪɴ](https://t.me/nextronsupport)\n"
                      "𝚂𝚄𝙿𝙿𝙾𝚁𝚃 𝙶𝚁𝙾𝚄𝙿           : [ᴊᴏɪɴ](https://t.me/nextronsupport)\n"
                      "𝘾𝙊𝙋𝙔𝙍𝙄𝙂𝙃𝙏 𝘽𝙔            : [ NEXTRON](https://t.me/nextronsupport)\n"
                                "[ ┏┓━┏┓━━━━┏┓━┏┓━━━━━\n ┃┃━┃┃━━━━┃┃━┃┃━━━━━\n ┃┗━┛┃┏━━┓┃┃━┃┃━┏━━┓\n ┃┏━┓┃┃┏┓┃┃┃━┃┃━┃┏┓┃ \n ┃┃━┃┃┃┃━┫┃┗┓┃┗┓┃┗┛┃ \n ┗┛━┗┛┗━━┛┗━┛┗━┛┗━━┛](https://t.me/teamishere)" , link_preview = False) 
        await alive.delete()
