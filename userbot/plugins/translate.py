import emoji
from googletrans import Translator

from hellbot.utils import *
from userbot.cmdhelp import CmdHelp

@bot.on(admin_cmd(pattern="trt ?(.*)"))
@bot.on(sudo_cmd(pattern="trt ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if "trim" in event.raw_text:
        # https://t.me/c/1220993104/192075
        return
    input_str = event.pattern_match.group(1)
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        text = previous_message.message
        lan = input_str or "ml"
    elif "|" in input_str:
        lan, text = input_str.split("|")
    else:
        await edit_or_reply(
            event,
            f"`.trt LanguageCode` as reply to a message.\nTry `.trc` to get all language codes",
        )
        return
    text = emoji.demojize(text.strip())
    lan = lan.strip()
    translator = Translator()
    try:
        translated = translator.translate(text, dest=lan)
        after_tr_text = translated.text
        # TODO: emojify the :
        # either here, or before translation
        output_str = """**Translated**\nFrom {} to {}
{}""".format(
            translated.src, lan, after_tr_text
        )
        await edit_or_reply(event, output_str)
    except Exception as exc:
        await edit_or_reply(event, str(exc))

@bot.on(admin_cmd(pattern=r"trc", outgoing=True))
@bot.on(sudo_cmd(pattern=r"trc", allow_sudo=True))
async def _(hell):
    if hell.fwd_from:
        return
    await edit_or_reply(hell, "**All The Language Codes Can Be Found** \n ⚡ [Here](https://telegra.ph/๖IGNIS乛-𐌰𐌽𐌰𐌽𐌳--ƒαkyeωσyaℓ-03-28) ⚡")



CmdHelp("translate").add_command(
  "trt", "<lang code> <reply to msg>", "Translates the replied message to desired language code. Type '.trc' to get all the language codes"
).add_command(
  "trc", None, "Gets all the possible language codes for google translate module"
).add()
