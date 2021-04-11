import string

from telethon.tl.types import Channel

from hellbot.utils import admin_cmd, edit_or_reply, sudo_cmd
from userbot import CMD_HELP
from userbot.cmdhelp import CmdHelp
from userbot.Config import Config

global msg_cache
msg_cache = {}


global groupsid
groupsid = []


async def all_groups_id(hell):
    hellgroups = []
    async for dialog in hell.client.iter_dialogs():
        entity = dialog.entity
        if isinstance(entity, Channel) and entity.megagroup:
            hellgroups.append(entity.id)
    return hellgroups


@bot.on(admin_cmd(pattern="frwd$"))
@bot.on(sudo_cmd(pattern="frwd$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if Config.PRIVATE_GROUP_BOT_API_ID is None:
        await edit_or_reply(
            event,
            "Please set the required environment variable `PRIVATE_GROUP_BOT_API_ID` for this plugin to work",
        )
        return
    try:
        e = await event.client.get_entity(Config.PRIVATE_GROUP_BOT_API_ID)
    except Exception as e:
        await edit_or_reply(event, str(e))
    else:
        re_message = await event.get_reply_message()
        # https://t.me/telethonofftopic/78166
        fwd_message = await event.client.forward_messages(e, re_message, silent=True)
        await event.client.forward_messages(event.chat_id, fwd_message)
        await event.delete()


@bot.on(admin_cmd(pattern="resend$"))
@bot.on(sudo_cmd(pattern="resend$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    try:
        await event.delete()
    except:
        pass
    m = await event.get_reply_message()
    if not m:
        return
    await event.respond(m)


@bot.on(admin_cmd(pattern=r"fpost (.*)"))
@bot.on(sudo_cmd(pattern=r"fpost (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    global groupsid
    global msg_cache
    await event.delete()
    text = event.pattern_match.group(1)
    destination = await event.get_input_chat()
    if len(groupsid) == 0:
        groupsid = await all_groups_id(event)
    for c in text.lower():
        if c not in string.ascii_lowercase:
            continue
        if c not in msg_cache:
            async for msg in event.client.iter_messages(event.chat_id, search=c):
                if msg.raw_text.lower() == c and msg.media is None:
                    msg_cache[c] = msg
                    break
        if c not in msg_cache:
            for i in groupsid:
                async for msg in event.client.iter_messages(event.chat_id, search=c):
                    if msg.raw_text.lower() == c and msg.media is None:
                        msg_cache[c] = msg
                        break
        await event.client.forward_messages(destination, msg_cache[c])


CmdHelp("fpost").add_command(
  'fpost', '<your msg>', 'Checks all your groups and sends the msg matching the given keyword'
).add_command(
  'frwd', '<reply to a msg>', 'Enables seen counter in replied msg. To know how many users have seen your msg.'
).add_command(
  'resend', '<reply to a msg>', 'Just resends the replied msg'
).add()
