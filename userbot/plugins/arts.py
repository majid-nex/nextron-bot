from userbot import ALIVE_NAME, CMD_HELP
from hellbot.utils import admin_cmd, edit_or_reply, sudo_cmd
from userbot.cmdhelp import CmdHelp

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Hell User"

USERID = bot.uid

mention = f"[{DEFAULTUSER}](tg://user?id={USERID})"

@bot.on(admin_cmd(pattern="carry (.*)"))
@bot.on(sudo_cmd(pattern="carry (.*)", allow_sudo=True))
async def kraken(carry):
    if carry.fwd_from:
        return
    name = carry.pattern_match.group(1)
    await edit_or_reply(
        carry,
        f"**Carry ~> {name} .**\n\n                     ⣤⣶⣶⣶⣦⣤⣄⡀\n⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀\n⠀⠀⠀⢀⣾⣿⣿⣿⠿⠿⠟⠻⠿⢿⣿⣿⣿⡆\n⠀⠀⠀⢰⣿⣿⡿⠂⠀⠀⠀⠀⠀⠀ ⠈⠉⢻⡇ \n⠀⠀⠀⠈⠿⣿⣇⣠⠤⠤⠤⢤⣀⣤⠤⠤⣺⡏ \n⠀⠀⠀⠀⠐⢉⣯⠹⣀⣀⣢⡸⠉⢏⡄⣀⣯⠁ \n⠀⠀⠀⠀⠡⠀⢹⣆⠀⠀⠀⣀⡀⡰⠀⢠⠖⠂ \n⠀⠀⠀⠀⠀⠈⠙⣿⣿⠀⠠⠚⢋⡁⠀⡜ \n⠀⠀⠀⠀⠀⠀⢸⠈⠙⠦⣤⣀⣤⣤⡼⠁  \n⠀⠀⠀ ⠀⢀⡌⠀⠀⠀⠀ ⠉⢏⡉  \n⠀⠀⠀⣀⣴⣿⣷⣶⣤⣤⣤⣴⣾⣷⣶⣦⡀ \n⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄ \n⠚⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛",
    )


@bot.on(admin_cmd(pattern="ded (.*)"))
@bot.on(sudo_cmd(pattern="ded (.*)", allow_sudo=True))
async def kraken(ded):
    if ded.fwd_from:
        return
    name = ded.pattern_match.group(1)
    await edit_or_reply(
        ded,
        f"{mention} --- {name}          \n　　　　　|"
        "\n　　　　　| \n"
        "　　　　　| \n"
        "　　　　　| \n"
        "　　　　　| \n"
        "　　　　　| \n"
        "　　　　　| \n"
        "　　　　　| \n"
        "　／￣￣＼| \n"
        "＜ ´･ 　　 |＼ \n"
        "　|　３　 | 丶＼ \n"
        "＜ 、･　　|　　＼ \n"
        "　＼＿＿／∪ _ ∪) \n"
        "　　　　　 Ｕ Ｕ\n",
    )


A = (
    "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
    "⠀⠀⠀⠀⠀⠀⠀⢀⣤⣤⡀⠀⠀⠀⠀⠀⠀\n"
    "⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀\n"
    "⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⠟⠀⠀⠀⠀⠀⠀\n"
    "⠀⠀⠀⠀⠀⠀⠀⠘⠻⣿⣷⣄⠀⠀⠀⠀⠀\n"
    "⠀⠀⠀⠀⣴⣶⣿⡆⠀⠀⠉⠉⠀⠈⣶⡆⠀\n"
    "⠀⠀⠀⢠⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⢻⣷⠀\n"
    "⠀⠀⠀⣼⣿⡿⠟⠀⠀⠀⠀⠀⠀⠀⣸⣿⡄\n"
    "⠀⠀⠀⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣷\n"
    "⠀⠀⠘⠛⠃⠀⠀⠀⠀⠀⠀⠀⠀⢰⣾⣿⠏\n"
    "⠀⢠⣧⡔⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠟⠁⠀\n"
    "⠀⢸⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ Ah\n shit, here we go again.\n"
)


@bot.on(admin_cmd(pattern="sthink (.*)"))
@bot.on(sudo_cmd(pattern="sthink (.*)", allow_sudo=True))
async def kraken(think):
    if think.fwd_from:
        return
    name = think.pattern_match.group(1)
    B = (
        f"**{mention} ~> {name} .\n\n**"
        "⠀⠀⠀⠀⢀⣀⣀⣀\n"
        "⠀⠀⠀⠰⡿⠿⠛⠛⠻⠿⣷\n"
        "⠀⠀⠀⠀⠀⠀⣀⣄⡀⠀⠀⠀⠀⢀⣀⣀⣤⣄⣀⡀\n"
        "⠀⠀⠀⠀⠀⢸⣿⣿⣷⠀⠀⠀⠀⠛⠛⣿⣿⣿⡛⠿⠷\n"
        "⠀⠀⠀⠀⠀⠘⠿⠿⠋⠀⠀⠀⠀⠀⠀⣿⣿⣿⠇\n"
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠁\n"
        "⠀\n"
        "⠀⠀⠀⠀⣿⣷⣄⠀⢶⣶⣷⣶⣶⣤⣀\n"
        "⠀⠀⠀⠀⣿⣿⣿⠀⠀⠀⠀⠀⠈⠙⠻⠗\n"
        "⠀⠀⠀⣰⣿⣿⣿⠀⠀⠀⠀⢀⣀⣠⣤⣴⣶⡄\n"
        "⠀⣠⣾⣿⣿⣿⣥⣶⣶⣿⣿⣿⣿⣿⠿⠿⠛⠃\n"
        "⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄\n"
        "⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡁\n"
        "⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁\n"
        "⠀⠀⠛⢿⣿⣿⣿⣿⣿⣿⡿⠟\n"
    )
    await edit_or_reply(think, B)


@bot.on(admin_cmd(pattern="sfrog (.*)"))
@bot.on(sudo_cmd(pattern="sfrog (.*)", allow_sudo=True))
async def kraken(frogsay):
    if frogsay.fwd_from:
        return
    name = frogsay.pattern_match.group(1)
    C = (
        f"**{mention} ~> {name} .\n\n**"
        "⠄⠄⠄⠄⠄⣀⣀⣤⣶⣿⣿⣶⣶⣶⣤⣄⣠⣴⣶⣿⣶⣦⣄⠄\n"
        "⠄⣠⣴⣾⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦\n"
        "⢠⠾⣋⣭⣄⡀⠄⠙⠻⣿⣿⡿⠛⠋⠉⠉⠉⠙⠛⠿⣿⣿⣿⣿\n"
        "⡎⡟⢻⣿⣷⠄⠄⠄⠄⡼⣡⣾⣿⣿⣦⠄⠄⠄⠄⠄⠈⠛⢿⣿\n"
        "⡇⣷⣾⣿⠟⠄⠄⠄⢰⠁⣿⣇⣸⣿⣿⠄⠄⠄⠄⠄⠄⠄⣠⣼\n"
        "⣦⣭⣭⣄⣤⣤⣴⣶⣿⣧⡘⠻⠛⠛⠁⠄⠄⠄⠄⣀⣴⣿⣿⣿\n"
        "⢉⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣦⣶⣶⣶⣶⣿⣿⣿⣿⣿⣿\n"
        "⡿⠛⠛⠛⠛⠻⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
        "⡇⠄⠄⢀⣀⣀⠄⠄⠄⠄⠉⠉⠛⠛⠻⠿⣿⣿⣿⣿⣿⣿⣿⣿\n"
        "⠈⣆⠄⠄⢿⣿⣿⣷⣶⣶⣤⣤⣀⣀⡀⠄⠄⠉⢻⣿⣿⣿⣿⣿\n"
        "⠄⣿⡀⠄⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠂⠄⢠⣿⣿⣿⣿⣿\n"
        "⠄⣿⡇⠄⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠄⢀⣼⣿⣿⣿⣿⣿\n"
        "⠄⣿⡇⠄⠠⣿⣿⣿⣿⣿⣿⣿⡿⠋⠄⠄⣠⣾⣿⣿⣿⣿⣿⣿\n"
        "⠄⣿⠁⠄⠐⠛⠛⠛⠉⠉⠉⠉⠄⠄⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿\n"
        "⠄⠻⣦⣀⣀⣀⣀⣀⣤⣤⣤⣤⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋\n"
    )
    await edit_or_reply(frogsay, C)


@bot.on(admin_cmd(pattern="sdead (.*)"))
@bot.on(sudo_cmd(pattern="sdead (.*)", allow_sudo=True))
async def kraken(deadfrog):
    if deadfrog.fwd_from:
        return
    name = deadfrog.pattern_match.group(1)
    D = (
        f"**{mention} ~> {name} .\n\n**"
        "⣿⣿⣿⡇⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
        "⣿⣿⣿⡇⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
        "⣿⣿⣿⡇⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
        "⣿⣿⣿⡇⠄⣿⣿⣿⡿⠋⣉⣉⣉⡙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
        "⣿⣿⣿⠃⠄⠹⠟⣡⣶⢟⣛⣛⡻⢿⣦⣩⣤⣬⡉⢻⣿⣿⣿⣿\n"
        "⣿⣿⣿⠄⢀⢤⣾⣿⣿⣿⡿⠿⠿⠿⢮⡃⣛⡻⢿⠈⣿⣿⣿⣿\n"
        "⣿⡟⢡⣴⣯⣿⣿⣿⠤⣤⣭⣶⣶⣶⣮⣔⡈⠛⢓⠦⠈⢻⣿⣿\n"
        "⠏⣠⣿⣿⣿⣿⣿⣿⣯⡪⢛⠿⢿⣿⣿⣿⡿⣼⣿⣿⣮⣄⠙⣿\n"
        "⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣾⡭⠴⣶⣶⣽⣽⣛⡿⠿⠿⠇⣿\n"
        "⣿⣿⣿⣿⣿⣿⣿⠿⣿⣿⣿⣿⣿⣿⣿⣷⣝⣛⢛⢋⣥⣴⣿⣿\n"
        "⣿⣿⣿⣿⣿⢿⠱⣿⣛⠾⣭⣛⡿⢿⣿⣿⣿⣿⣿⡀⣿⣿⣿⣿\n"
        "⠑⠽⡻⢿⣮⣽⣷⣶⣯⣽⣳⠮⣽⣟⣲⠯⢭⣿⣛⡇⣿⣿⣿⣿\n"
        "⠄⠄⠈⠑⠊⠉⠟⣻⠿⣿⣿⣿⣷⣾⣭⣿⠷⠶⠂⣴⣿⣿⣿⣿\n"
        "⠄⠄⠄⠄⠄⠄⠄⠁⠙⠒⠙⠯⠍⠙⢉⣡⣶⣿⣿⣿⣿⣿⣿⣿\n"
        "⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
    )
    await edit_or_reply(deadfrog, D)


@bot.on(admin_cmd(pattern="strump (.*)"))
@bot.on(sudo_cmd(pattern="strump (.*)", allow_sudo=True))
async def kraken(trumpsay):
    if trumpsay.fwd_from:
        return
    name = trumpsay.pattern_match.group(1)
    E = (
        f"**Donald Trump ~> {name} .\n\n**"
        "⣿⣿⣿⣿⣿⣿⡿⠿⠛⠋⠉⡉⣉⡛⣛⠿⣿⣿⣿⣿⣿⣿⣿⣿\n"
        "⣿⣿⣿⡿⠋⠁⠄⠄⠄⠄⠄⢀⣸⣿⣿⡿⠿⡯⢙⠿⣿⣿⣿⣿\n"
        "⣿⣿⡿⠄⠄⠄⠄⠄⡀⡀⠄⢀⣀⣉⣉⣉⠁⠐⣶⣶⣿⣿⣿⣿\n"
        "⣿⣿⡇⠄⠄⠄⠄⠁⣿⣿⣀⠈⠿⢟⡛⠛⣿⠛⠛⣿⣿⣿⣿⣿\n"
        "⣿⣿⡆⠄⠄⠄⠄⠄⠈⠁⠰⣄⣴⡬⢵⣴⣿⣤⣽⣿⣿⣿⣿⣿\n"
        "⣿⣿⡇⠄⢀⢄⡀⠄⠄⠄⠄⡉⠻⣿⡿⠁⠘⠛⡿⣿⣿⣿⣿⣿\n"
        "⣿⡿⠃⠄⠄⠈⠻⠄⠄⠄⠄⢘⣧⣀⠾⠿⠶⠦⢳⣿⣿⣿⣿⣿\n"
        "⣿⣶⣤⡀⢀⡀⠄⠄⠄⠄⠄⠄⠻⢣⣶⡒⠶⢤⢾⣿⣿⣿⣿⣿\n"
        "⣿⡿⠋⠄⢘⣿⣦⡀⠄⠄⠄⠄⠄⠉⠛⠻⠻⠺⣼⣿⠟⠛⠿⣿\n"
        "⠋⠁⠄⠄⠄⢻⣿⣿⣶⣄⡀⠄⠄⠄⠄⢀⣤⣾⣿⡀⠄⠄⠄⢹\n"
        "⠄⠄⠄⠄⠄⠄⢻⣿⣿⣿⣷⡤⠄⠰⡆⠄⠄⠈⠛⢦⣀⡀⡀⠄\n"
        "⠄⠄⠄⠄⠄⠄⠈⢿⣿⠟⡋⠄⠄⠄⢣⠄⠄⠄⠄⠄⠈⠹⣿⣀\n"
        "⠄⠄⠄⠄⠄⠄⠄⠘⣷⣿⣿⣷⠄⠄⢺⣇⠄⠄⠄⠄⠄⠄⠸⣿\n"
        "⠄⠄⠄⠄⠄⠄⠄⠄⠹⣿⣿⡇⠄⠄⠸⣿⡄⠄⠈⠁⠄⠄⠄⣿\n"
        "⠄⠄⠄⠄⠄⠄⠄⠄⠄⢻⣿⡇⠄⠄⠄⢹⣧⠄⠄⠄⠄⠄⠄⠘\n"
    )
    await edit_or_reply(trumpsay, E)


@bot.on(admin_cmd(pattern="schina (.*)"))
@bot.on(sudo_cmd(pattern="schina (.*)", allow_sudo=True))
async def kraken(ckmkb):
    if ckmkb.fwd_from:
        return
    name = ckmkb.pattern_match.group(1)
    F = (
        f"**🅲🅺🅼🅺🅱 ~> {name} .\n\n**"
        "⣿⣿⣿⣿⠟⠋⢁⢁⢁⢁⢁⢁⢁⢁⠈⢻⢿⣿⣿⣿⣿⣿⣿⣿\n"
        "⣿⣿⣿⣿⠃⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⡀⠭⢿⣿⣿⣿⣿\n"
        "⣿⣿⣿⡟⠄⢀⣾⣿⣿⣿⣷⣶⣿⣷⣶⣶⡆⠄⠄⠄⣿⣿⣿⣿\n"
        "⣿⣿⣿⡇⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠄⠄⢸⣿⣿⣿⣿\n"
        "⣿⣿⣿⣇⣼⣿⣿⠿⠶⠙⣿⡟⠡⣴⣿⣽⣿⣧⠄⢸⣿⣿⣿⣿\n"
        "⣿⣿⣿⣿⣾⣿⣿⣟⣭⣾⣿⣷⣶⣶⣴⣶⣿⣿⢄⣿⣿⣿⣿⣿\n"
        "⣿⣿⣿⣿⣿⣿⣿⡟⣩⣿⣿⣿⡏⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
        "⣿⣿⣿⣿⣿⣹⡋⠘⠷⣦⣀⣠⡶⠁⠈⠁⠄⣿⣿⣿⣿⣿⣿⣿\n"
        "⣿⣿⣿⣿⣿⣍⠃⣴⣶⡔⠒⠄⣠⢀⠄⠄⠄⡨⣿⣿⣿⣿⣿⣿\n"
        "⣿⣿⣿⣿⣿⣿⣦⡘⠿⣷⣿⠿⠟⠃⠄⠄⣠⡇⠈⠻⣿⣿⣿⣿\n"
        "⣿⣿⣿⡿⠟⠋⢁⣷⣠⠄⠄⠄⠄⣀⣠⣾⡟⠄⠄⠄⠄⠉⠙⠻\n"
        "⡿⠟⠁⠄⠄⠄⢸⣿⣿⡯⢓⣴⣾⣿⣿⡟⠄⠄⠄⠄⠄⠄⠄⠄\n"
        "⠄⠄⠄⠄⠄⠄⣿⡟⣷⠄⠹⣿⣿⣿⡿⠁⠄⠄⠄⠄⠄⠄⠄⠄\n"
        "⠄⠄⠄⠄⠄⣸⣿⡷⡇⠄⣴⣾⣿⣿⠃⠄⠄⠄⠄⠄⠄⠄⠄⠄\n"
        "⠄⠄⠄⠄⠄⣿⣿⠃⣦⣄⣿⣿⣿⠇⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄\n"
        "⠄⠄⠄⠄⢸⣿⠗⢈⡶⣷⣿⣿⡏⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄\n"
    )
    await edit_or_reply(ckmkb, F)


@bot.on(admin_cmd(pattern=r"sshit$"))
@bot.on(sudo_cmd(pattern="sshit$", allow_sudo=True))
async def kraken(shit):
    if shit.fwd_from:
        return
    await edit_or_reply(shit, A)


@bot.on(admin_cmd(pattern=r"elove$"))
@bot.on(sudo_cmd(pattern="elove$", allow_sudo=True))
async def kakashi(event):
    if event.fwd_from:
        return
    await edit_or_reply(
        event,
        "░░▄███▄███▄\n░░█████████\n░░▒▀█████▀░\n░░▒░░▀█▀\n░░▒░░█░\n░░▒░█\n░░░█\n░░█░░░░███████\n░██░░░██▓▓███▓██▒\n██░░░█▓▓▓▓▓▓▓█▓████\n██░░██▓▓▓(◐)▓█▓█▓█\n███▓▓▓█▓▓▓▓▓█▓█▓▓▓▓█\n▀██▓▓█░██▓▓▓▓██▓▓▓▓▓█\n░▀██▀░░█▓▓▓▓▓▓▓▓▓▓▓▓▓█\n░░░░▒░░░█▓▓▓▓▓█▓▓▓▓▓▓█\n░░░░▒░░░█▓▓▓▓█▓█▓▓▓▓▓█\n░▒░░▒░░░█▓▓▓█▓▓▓█▓▓▓▓█\n░▒░░▒░░░█▓▓▓█░░░█▓▓▓█\n░▒░░▒░░██▓██░░░██▓▓██\n██████████████████████\n█─████─▄▄─██─█─██─▄▄─█\n█─██▀█─██─██─█─██─▄█▀█\n█▄▄▄▄▀▄▄▄▄▀▀▄▄▄▀▀▄▄▄▄▀",
    )


G = (
    "▄███████▄\n"
    "█▄█████▄█\n"
    "█▼▼▼▼▼█\n"
    "██________█▌\n"
    "█▲▲▲▲▲█\n"
    "█████████\n"
    "_████\n"
)

H = (
    "┈┈┏━╮╭━┓┈╭━━━━╮\n"
    "┈┈┃┏┗┛┓┃╭┫ⓞⓘⓝⓚ┃\n"
    "┈┈╰┓▋▋┏╯╯╰━━━━╯\n"
    "┈╭━┻╮╲┗━━━━╮╭╮┈\n"
    "┈┃▎▎┃╲╲╲╲╲╲┣━╯┈\n"
    "┈╰━┳┻▅╯╲╲╲╲┃┈┈┈\n"
    "┈┈┈╰━┳┓┏┳┓┏╯┈┈┈\n"
    "┈┈┈┈┈┗┻┛┗┻┛┈┈┈┈\n"
)

I = (
    "░▐█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█▄\n"
    "░███████████████████████ \n"
    "░▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓◤ \n"
    "░▀░▐▓▓▓▓▓▓▌▀█░░░█▀░\n"
    "░░░▓▓▓▓▓▓█▄▄▄▄▄█▀░░\n"
    "░░█▓▓▓▓▓▌░░░░░░░░░░\n"
    "░▐█▓▓▓▓▓░░░░░░░░░░░\n"
    "░▐██████▌░░░░░░░░░░\n"
)

J = (
    "╥━━━━━━━━╭━━╮━━┳\n"
    "╢╭╮╭━━━━━┫┃▋▋━▅┣\n"
    "╢┃╰┫┈┈┈┈┈┃┃┈┈╰┫┣\n"
    "╢╰━┫┈┈┈┈┈╰╯╰┳━╯┣\n"
    "╢┊┊┃┏┳┳━━┓┏┳┫┊┊┣\n"
    "╨━━┗┛┗┛━━┗┛┗┛━━┻\n"
)
K = "╔┓┏╦━╦┓╔┓╔━━╗\n" "║┗┛║┗╣┃║┃║X X║\n" "║┏┓║┏╣┗╣┗╣╰╯║\n" "╚┛┗╩━╩━╩━╩━━╝\n"

L = (
    "▬▬▬.◙.▬▬▬ \n"
    "═▂▄▄▓▄▄▂ \n"
    "◢◤ █▀▀████▄▄▄▄◢◤ \n"
    "█▄ █ █▄ ███▀▀▀▀▀▀▀╬ \n"
    "◥█████◤ \n"
    "══╩══╩══ \n"
    "╬═╬ \n"
    "╬═╬ \n"
    "╬═╬ \n"
    "╬═╬ \n"
    "╬═╬ \n"
    "╬═╬ \n"
    "╬═╬ Hello, My Friend :D \n"
    "╬═╬☻/ \n"
    "╬═╬/▌ \n"
    "╬═╬/ \\n"
)

M = (
    "┳┻┳┻╭━━━━╮╱▔▔▔╲\n"
    "┻┳┻┳┃╯╯╭━┫▏╰╰╰▕\n"
    "┳┻┳┻┃╯╯┃▔╰┓▔▂▔▕╮\n"
    "┻┳┻┳╰╮╯┃┈╰┫╰━╯┏╯\n"
    "┳┻┳┻┏╯╯┃╭━╯┳━┳╯\n"
    "┻┳┻┳╰━┳╯▔╲╱▔╭╮▔╲\n"
    "┳┻┳┻┳┻┃┈╲┈╲╱╭╯╮▕\n"
    "┻┳┻┳┻┳┃┈▕╲▂╱┈╭╯╱\n"
    "┳┻┳┻┳┻┃'''┈┃┈┃┈'''╰╯\n"
    "┻┳┻┳┻┏╯▔'''╰┓┣━┳┫\n"
    "┳┻┳┻┳╰┳┳┳'''╯┃┈┃┃\n"
    "┻┳┻┳┻┳┃┃┃┈'''┃┈┃┃\n"
    "┳┻┳┻┳┻┃┃┃'''┊┃┈┃┃\n"
    "┻┳┻┳┻┳┃┃┃┈'''┃┈┃┃.\n"
    "┳┻┳┻┳┻┣╋┫'''┊┣━╋┫\n"
    "┻┳┻┳┻╭╯╰╰-╭╯━╯.''╰╮\n"
    "Love You Forever,,,,\n"
)

N = (
    "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⡿⠋⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⠀⠀⣠⣾⣿⡿⠋⠀⠀⠉⠻⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⠀⠀⣿⣿⣿⠃⠀⠀⣀⡀⠀⢹⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⡄⠀⠙⠻⠋⠀⠀⣸⣿⣿⠀⠀⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⣰⣿⣿⠟⠀⢠⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⡿⠛⠛⠒⠶⠾⢿⣿⣿⣷⣄⣾⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⠀⢰⣿⣿⣷⣶⣦⣼⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⡀⠀⠙⠻⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⢿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⠀⠀⠀⠉⠉⠛⠛⠛⠶⢶⣤⣼⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣦⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⠁⠀⣾⣿⣷⡄⠀⢼⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⠀⠀⢿⣿⣿⡿⠀⠈⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⣇⠀⠀⠉⠋⠁⠀⢠⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⠿⢷⣤⣀⣀⣀⣠⣾⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⠀⠀⠀⠈⠉⠉⠛⢻⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⣶⣦⣤⣤⣀⠀⠀⢸⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠹⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⡿⠛⠉⠉⠙⠻⣀⣀⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⠁⠀⣀⡀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⠀⢸⣿⡇⠀⣷⡀⠘⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⡄⠈⢻⡇⠀⡿⠃⠀⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⣷⣄⢸⡇⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⠀⠉⠉⠑⠒⠲⠿⢿⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⣤⣄⣀⡀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⢺⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⠀⠀⠉⠉⠙⠋⠀⠀⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⣤⣤⣀⣀⡀⠀⠀⣰⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣷⠀⢹⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⠀⠀⠀⠉⠉⠉⠀⠀⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⣶⣤⣤⣀⣀⣀⣀⣰⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⡟⠉⠀⠀⠈⠙⢿⣿⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⠀⢀⣤⡄⠀⡀⠀⢹⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⠀⢸⣿⡇⠀⣿⡄⠈⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⡆⠀⢹⡇⠀⠟⠁⢀⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⣿⣦⣸⡇⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
)

O = (
    "⣿⣿⣿⣿⣿⣍⠀⠉⠻⠟⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⠓⠀⠀⢒⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⣿\n"
    "⣿⡿⠋⠋⠀⠀⠀⠀⠀⠀⠈⠙⠻⢿⢿⣿⣿⡿⣿⣿⡟⠋⠀⢀⣩\n"
    "⣿⣿⡄⠀⠀⠀⠀⠀⠁⡀⠀⠀⠀⠀⠈⠉⠛⢷⣭⠉⠁⠀⠀⣿⣿\n"
    "⣇⣀. INDIA🇮🇳INDIA🇮🇳⠆⠠..⠘⢷⣿⣿⣛⠐⣶⣿⣿\n"
    "⣿⣄⠀⣰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⢀⣠⣿⣿⣿⣾⣿⣿⣿\n"
    "⣿⣿⣿⣿⠀⠀⠀⠀⡠⠀⠀⠀⠀⠀⢀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠄⠀⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⣠⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⠀⠀⠂⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣇⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⡆⠀⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⣿⣦⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
)

P = (
    "───▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄───\n"
    "───█▒▒░░░░░░░░░▒▒█───\n"
    "────█░░█░░░░░█░░█────\n"
    "─▄▄──█░░░▀█▀░░░█──▄▄─\n"
    "█░░█─▀▄░░░░░░░▄▀─█░░█\n"
    "█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█\n"
    "█░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█\n"
    "█░░║║║╠─║─║─║║║║║╠─░░█\n"
    "█░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█\n"
    "█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n"
)

Q = (
    "░░░░▓\n"
    "░░░▓▓\n"
    "░░█▓▓█\n"
    "░██▓▓██\n"
    "░░██▓▓██\n"
    "░░░██▓▓██\n"
    "░░░░██▓▓██\n"
    "░░░░░██▓▓██\n"
    "░░░░██▓▓██\n"
    "░░░██▓▓██\n"
    "░░██▓▓██\n"
    "░██▓▓██\n"
    "░░██▓▓██\n"
    "░░░██▓▓██\n"
    "░░░░██▓▓██\n"
    "░░░░░██▓▓██\n"
    "░░░░██▓▓██\n"
    "░░░██▓▓██\n"
    "░░██▓▓██\n"
    "░██▓▓██\n"
    "░░██▓▓██\n"
    "░░░██▓▓██\n"
    "░░░░██▓▓██\n"
    "░░░░░██▓▓██\n"
    "░░░░██▓▓██\n"
    "░░░██▓▓██\n"
    "░░██▓▓██\n"
    "░██▓▓██\n"
    "░░██▓▓██\n"
    "░░░██▓▓██\n"
    "░░░░██▓▓██\n"
    "░░░░░██▓▓██\n"
    "░░░░██▓▓██\n"
    "░░░██▓▓██\n"
    "░░██▓▓██\n"
    "░██▓▓██\n"
    "░░██▓▓██\n"
    "░░░██▓▓██\n"
    "░░░░██▓▓██\n"
    "░░░░░██▓▓██\n"
    "░░░░██▓▓██\n"
    "░░░██▓▓██\n"
    "░░██▓▓██\n"
    "░██▓▓██\n"
    "░░██▓▓██\n"
    "░░░██▓▓██\n"
    "░░░░██▓▓██\n"
    "░░░░░██▓▓██\n"
    "░░░░██▓▓██\n"
    "░░░██▓▓██\n"
    "░░██▓▓██\n"
    "░██▓▓██\n"
    "░░██▓▓██\n"
    "░░░██▓▓██\n"
    "░░░░██▓▓██\n"
    "░░░░░██▓▓██\n"
    "░░░░██▓▓██\n"
    "░░░██▓▓██\n"
    "░░██▓▓██\n"
    "░██▓▓██\n"
    "░░██▓▓██\n"
    "░░░██▓▓██\n"
    "░░░░██▓▓██\n"
    "░░░░░██▓▓██\n"
    "░░░░██▓▓██\n"
    "░░░██▓▓██\n"
    "░░██▓▓██\n"
    "░░██▓▓██\n"
    "░░██▓▓██\n"
    "░░██▓▓██\n"
    "░░██▓▓██\n"
    "░░██▓▓██\n"
    "░░░██▓▓███\n"
    "░░░░██▓▓████\n"
    "░░░░░██▓▓█████\n"
    "░░░░░░██▓▓██████\n"
    "░░░░░░███▓▓███████\n"
    "░░░░░████▓▓████████\n"
    "░░░░█████▓▓█████████\n"
    "░░░█████░░░█████●███\n"
    "░░████░░░░░░░███████\n"
    "░░███░░░░░░░░░██████\n"
    "░░██░░░░░░░░░░░████\n"
    "░░░░░░░░░░░░░░░░███\n"
    "░░░░░░░░░░░░░░░░░░░\n"
)


R = (
    "────██──────▀▀▀██\n"
    "──▄▀█▄▄▄─────▄▀█▄▄▄\n"
    "▄▀──█▄▄──────█─█▄▄\n"
    "─▄▄▄▀──▀▄───▄▄▄▀──▀▄\n"
    "─▀───────▀▀─▀───────▀▀\n🚶🏻‍♂️🚶🏻‍♂️ɮʏɛ ʄʀɨɛռɖֆ.."
)

S = (
    "╭━━━┳╮╱╱╭╮╱╭━━━┳━━━╮\n"
    "┃╭━╮┃┃╱╭╯╰╮┃╭━╮┃╭━╮┃\n"
    "┃╰━━┫╰━╋╮╭╯┃┃╱┃┃╰━━╮\n"
    "╰━━╮┃╭╮┣┫┃╱┃┃╱┃┣━━╮┃\n"
    "┃╰━╯┃┃┃┃┃╰╮┃╰━╯┃╰━╯┃\n"
    "╰━━━┻╯╰┻┻━╯╰━━━┻━━━╯\n"
)


T = (
    "███████▄▄███████████▄\n"
    "▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n"
    "▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n"
    "▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n"
    "▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n"
    "▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n"
    "▓▓▓▓▓▓███░░░░░░░░░░░░█\n"
    "██████▀░░█░░░░██████▀\n"
    "░░░░░░░░░█░░░░█\n"
    "░░░░░░░░░░█░░░█\n"
    "░░░░░░░░░░░█░░█\n"
    "░░░░░░░░░░░█░░█\n"
    "░░░░░░░░░░░░▀▀\n"
)


@bot.on(admin_cmd(pattern=r"monster$"))
@bot.on(sudo_cmd(pattern="monster$", allow_sudo=True))
async def bluedevilmonster(monster):
    if monster.fwd_from:
        return
    await edit_or_reply(monster, G)


@bot.on(admin_cmd(pattern=r"pig$"))
@bot.on(sudo_cmd(pattern="pig$", allow_sudo=True))
async def bluedevilpig(pig):
    if pig.fwd_from:
        return
    await edit_or_reply(pig, H)


@bot.on(admin_cmd(pattern=r"gun$"))
@bot.on(sudo_cmd(pattern="gun$", allow_sudo=True))
async def bluedevilgun(gun):
    if gun.fwd_from:
        return
    await edit_or_reply(gun, I)


@bot.on(admin_cmd(pattern=r"dog$"))
@bot.on(sudo_cmd(pattern="dog$", allow_sudo=True))
async def bluedevildog(dog):
    if dog.fwd_from:
        return
    await edit_or_reply(dog, J)


@bot.on(admin_cmd(pattern=r"hello$"))
@bot.on(sudo_cmd(pattern="hello$", allow_sudo=True))
async def bluedevilhello(hello):
    if hello.fwd_from:
        return
    await edit_or_reply(hello, K)


@bot.on(admin_cmd(pattern=r"hmf$"))
@bot.on(sudo_cmd(pattern="hmf$", allow_sudo=True))
async def bluedevilhmf(hmf):
    if hmf.fwd_from:
        return
    await edit_or_reply(hmf, L)


@bot.on(admin_cmd(pattern=r"couple$"))
@bot.on(sudo_cmd(pattern="couple$", allow_sudo=True))
async def bluedevilcouple(couple):
    if couple.fwd_from:
        return
    await edit_or_reply(couple, M)


@bot.on(admin_cmd(pattern=r"sup$"))
@bot.on(sudo_cmd(pattern="sup$", allow_sudo=True))
async def bluedevilsupreme(supreme):
    if supreme.fwd_from:
        return
    await edit_or_reply(supreme, N)


@bot.on(admin_cmd(pattern=r"india$"))
@bot.on(sudo_cmd(pattern="india$", allow_sudo=True))
async def bluedevilindia(event):
    if event.fwd_from:
        return
    await edit_or_reply(event, O)


@bot.on(admin_cmd(pattern=r"wc$"))
@bot.on(sudo_cmd(pattern="wc$", allow_sudo=True))
async def bluedevilwelcome(welcome):
    if welcome.fwd_from:
        return
    await edit_or_reply(welcome, P)


@bot.on(admin_cmd(pattern=r"snk$"))
@bot.on(sudo_cmd(pattern="snk$", allow_sudo=True))
async def bluedevilsnake(snake):
    if snake.fwd_from:
        return
    await edit_or_reply(snake, Q)


@bot.on(admin_cmd(pattern=r"bye$"))
@bot.on(sudo_cmd(pattern="bye$", allow_sudo=True))
async def bluedevilbye(bye):
    if bye.fwd_from:
        return
    await edit_or_reply(bye, R)


@bot.on(admin_cmd(pattern=r"shitos$"))
@bot.on(sudo_cmd(pattern="shitos$", allow_sudo=True))
async def bluedevilshitos(shitos):
    if shitos.fwd_from:
        return
    await edit_or_reply(shitos, S)


@bot.on(admin_cmd(pattern=r"dislike$"))
@bot.on(sudo_cmd(pattern="dislike$", allow_sudo=True))
async def bluedevildislike(dislike):
    if dislike.fwd_from:
        return
    await edit_or_reply(dislike, T)


CmdHelp("arts").add_command(
  'elove', None, 'Use and see'
).add_command(
  'monster', None, 'Use and see'
).add_command(
  'pig', None, 'Use and see'
).add_command(
  'gun', None, 'Use and see'
).add_command(
  'dog', None, 'Use and see'
).add_command(
  'hello', None, 'Use and see'
).add_command(
  'hmf', None, 'Use and see'
).add_command(
  'couple', None, 'Use and see'
).add_command(
  'sup', None, 'Use and see'
).add_command(
  'india', None, 'Use and see'
).add_command(
  'wc', None, 'Use and see'
).add_command(
  'snk', None, 'Use and see'
).add_command(
  'bye', None, 'Use and see'
).add_command(
  'shitos', None, 'Use and see'
).add_command(
  'dislike', None, 'Use and see'
).add_command(
  'carry', '<text>', 'send your text with carry art'
).add_command(
  'ded', '<text>', 'Hang yourself'
).add_command(
  'sthink', '<text>', 'Send your text in thinking art'
).add_command(
  'sfrog', '<text>', 'Send your text in frog art'
).add_command(
  'sdead', '<text>', 'Send your text in dear frog art'
).add_command(
  'strump', '<text>', 'Send your text in trump art'
).add_command(
  'china', '<text>', 'Send your text in china art'
).add_command(
  'sshit', None, 'Send a art in "Ahh shit. Here we go again"'
).add()
