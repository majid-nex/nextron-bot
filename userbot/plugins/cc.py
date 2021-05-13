from faker import Faker as dc
from userbot.utils import admin_cmd as devil_cmd
from userbot import bot as devil
@devil.on(devil_cmd("cc"))
async def _devil(dark):
    cyber = dc()
    killer = cyber.name()
    kali = cyber.address()
    alain = cyber.credit_card_full()
    await dark.edit(f"ℕ𝕒𝕞𝕖:-\n`{killer}`\n\n𝔸𝕕𝕕𝕣𝕖𝕤𝕤:-\n`{kali}`\n\nℂ𝕒𝕣𝕕:-\n`{alain}`")
