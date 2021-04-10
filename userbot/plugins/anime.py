import re

from userbot import bot
from userbot.utils import admin_cmd, sudo_cmd, edit_or_reply
from userbot.cmdhelp import CmdHelp
from userbot.helpers.functions import deEmojify


@bot.on(admin_cmd(pattern="anime(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="anime(?: |$)(.*)", allow_sudo=True))
async def nope(NEX-GEN):
    Nextron = NEX-GEN.pattern_match.group(1)
    if not Nextron:
        if NEX-GEN.is_reply:
            (await NEX-GEN.get_reply_message()).message
        else:
            await edit_or_reply(NEX-GEN, "`Sir please give some query to search and download it for you..!`"
            )
            return

    troll = await bot.inline_query("animedb_bot", f"{(deEmojify(nex))}")

    await troll[0].click(
        NEX-GEN.chat_id,
        reply_to=NEX-GEN.reply_to_msg_id,
        silent=True if NEX-GEN.is_reply else False,
        hide_via=True,
    )
    await NEX-GEN.delete()
    

CmdHelp("anime").add_command(
  "anime", "<anime name>", "Searches for the given anime and sends the details."
).add()
