""" Userbot module for keeping control who PM you. """
import asyncio
import io
from telethon.tl.functions.contacts import BlockRequest, UnblockRequest
from telethon.tl.functions.messages import ReportSpamRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import User
from sqlalchemy.exc import IntegrityError

from userbot import (COUNT_PM, CMD_HELP, LOGGER, LOGGER_GROUP,
                     PM_AUTO_BAN, LASTMSG, LOGS)


from userbot.events import register

# ========================= CONSTANTS ============================
UNAPPROVED_MSG = ("*Bleep Blop! This is a Bot. Don't fret* \n\n"
                  "`If You Are Hater then Maderchod Maa Chudao Bhosdike MaderHod`.`"
                  "`If You Are One Of My Friends Kindly Wait Till Me Come Online.`\n\n"
                  "`As far as i know, he doesn't usually approve Retards.`\n\n"
                  "`Spam Can make you blocked`")
# =================================================================


@register(incoming=True)
async def permitpm(event):
    """ Prohibits people from PMing you without approval. \
        Will block retarded nibbas automatically. """
    if PM_AUTO_BAN:
        self_user = await event.client.get_me()
        if event.is_private and event.chat_id != 777000 and event.chat_id != self_user.id and not (await event.get_sender()).bot:
            try:
                from userbot.modules.sql_helper.pm_permit_sql import is_approved
                from userbot.modules.sql_helper.globals import gvarstatus
            except AttributeError:
                return
            apprv = is_approved(event.chat_id)
            notifsoff = gvarstatus("NOTIF_OFF")

            # This part basically is a sanity check
            # If the message that sent before is Unapproved Message
            # then stop sending it again to prevent FloodHit
            if not apprv and event.text != UNAPPROVED_MSG:
                if event.chat_id in LASTMSG:
                    prevmsg = LASTMSG[event.chat_id]
                    # If the message doesn't same as previous one
                    # Send the Unapproved Message again
                    if event.text != prevmsg:
                        async for message in event.client.iter_messages(event.chat_id, 
                                                                        from_user='me', 
                                                                        search=UNAPPROVED_MSG, 
                                                                        limit=1):
                            await message.delete()
                        await event.reply(UNAPPROVED_MSG)
                    LASTMSG.update({event.chat_id: event.text})
                else:
                    await event.reply(UNAPPROVED_MSG)
                    LASTMSG.update({event.chat_id: event.text})

                if notifsoff:
                    await event.client.send_read_acknowledge(event.chat_id)
                if event.chat_id not in COUNT_PM:
                    COUNT_PM.update({event.chat_id: 1})
                else:
                    COUNT_PM[event.chat_id] = COUNT_PM[event.chat_id] + 1

                if COUNT_PM[event.chat_id] > 3:
                    await event.respond(
                        "`You were spamming my peru master's Inox.`\n"
                        "`You chuu nubfuk been BLOCKED and reported as SPAM, now GTFO.`"
                    )

                    try:
                        del COUNT_PM[event.chat_id]
                        del LASTMSG[event.chat_id]
                    except KeyError:
                        if LOGGER:
                            await event.client.send_message(
                                LOGGER_GROUP,
                                "Count PM is seemingly going retard, plis restart bot!",
                            )
                        LOGS.info("CountPM wen't rarted boi")
                        return

                    await event.client(BlockRequest(event.chat_id))
                    await event.client(ReportSpamRequest(peer=event.chat_id))

                    if LOGGER:
                        name = await event.client.get_entity(event.chat_id)
                        name0 = str(name.first_name)
                        await event.client.send_message(
                            LOGGER_GROUP,
                            "["
                            + name0
                            + "](tg://user?id="
                            + str(event.chat_id)
                            + ")"
                            + " was just another retarded nibba",
                        )

@register(outgoing=True)
async def auto_accept(event):
    """ Will approve automatically if you texted them first. """
    self_user = await event.client.get_me()
    if event.is_private and event.chat_id != 777000 and event.chat_id != self_user.id and not (await event.get_sender()).bot:
        try:
            from userbot.modules.sql_helper.pm_permit_sql import is_approved
            from userbot.modules.sql_helper.pm_permit_sql import approve
        except AttributeError:
            return

        chat = await event.get_chat()
        if isinstance(chat, User):
            if is_approved(event.chat_id) or chat.bot:
                return
            async for message in event.client.iter_messages(
                    event.chat_id, reverse=True, limit=1
            ):
                if message.message is not UNAPPROVED_MSG and message.from_id == (await event.client.get_me()).id:
                    try:
                        approve(event.chat_id)
                    except IntegrityError:
                        return

                if is_approved(event.chat_id) and LOGGER:
                    await event.client.send_message(
                        LOGGER_GROUP,
                        "#AUTO-APPROVED\n"
                        + "User: " +
                        f"[{chat.first_name}](tg://user?id={chat.id})",
                    )


@register(outgoing=True, pattern="^.notifoff$")
async def notifoff(noff_event):
    """ For .notifoff command, stop getting notifications from unapproved PMs. """
    if not noff_event.text[0].isalpha() and noff_event.text[0] not in ("/", "#", "@", "!"):
        try:
            from userbot.modules.sql_helper.globals import addgvar
        except AttributeError:
            return
        addgvar("NOTIF_OFF", True)
        await noff_event.edit("`Notifications from unapproved PM's are silenced!`")


@register(outgoing=True, pattern="^.notifon$")
async def notifon(non_event):
    """ For .notifoff command, get notifications from unapproved PMs. """
    if not non_event.text[0].isalpha() and non_event.text[0] not in ("/", "#", "@", "!"):
        try:
            from userbot.modules.sql_helper.globals import delgvar
        except AttributeError:
            return
        delgvar("NOTIF_OFF")
        await non_event.edit("`Notifications from unapproved PM's unmuted!`")

@register(outgoing=True, pattern="^.pm$")
async def approvepm(apprvpm):
    """ For .pm command, give someone the permissions to PM you. """
    if not apprvpm.text[0].isalpha() and apprvpm.text[0] not in ("/", "#", "@", "!"):
        try:
            from userbot.modules.sql_helper.pm_permit_sql import approve
        except AttributeError:
            await apprvpm.edit("`Running on Non-SQL mode!`")
            return

        if apprvpm.reply_to_msg_id:
            reply = await apprvpm.get_reply_message()
            replied_user = await apprvpm.client(GetFullUserRequest(reply.from_id))
            aname = replied_user.user.id
            name0 = str(replied_user.user.first_name)
            uid = replied_user.user.id

        else:
            aname = await apprvpm.client.get_entity(apprvpm.chat_id)
            name0 = str(aname.first_name)
            uid = apprvpm.chat_id

        try:
            approve(uid)
        except IntegrityError:
            await apprvpm.edit("`This boi may already be approved.`")
            return

        await apprvpm.edit(
            f"[{name0}](tg://user?id={uid}) ` #Maderbsdk Approved to PM uh Sir Kek!`"
        )

        async for message in apprvpm.client.iter_messages(apprvpm.chat_id, 
                                                          from_user='me', 
                                                          search=UNAPPROVED_MSG, 
                                                          limit=1):
            await message.delete()
            await apprvpm.delete()

        if LOGGER:
            await apprvpm.client.send_message(
                LOGGER_GROUP,
                "#APPROVED\n"
                + "User: " + f"[{name0}](tg://user?id={uid})",
            )



@register(outgoing=True, pattern="^.dis$")
async def disapprovepm(disapprvpm):
    if not disapprvpm.text[0].isalpha() and disapprvpm.text[0] not in ("/", "#", "@", "!"):
        try:
            from userbot.modules.sql_helper.pm_permit_sql import dissprove
        except:
            await disapprvpm.edit("`Running on Non-SQL mode!`")
            return

        if disapprvpm.reply_to_msg_id:
            reply = await disapprvpm.get_reply_message()
            replied_user = await disapprvpm.client(GetFullUserRequest(reply.from_id))
            aname = replied_user.user.id
            name0 = str(replied_user.user.first_name)
            dissprove(replied_user.user.id)
        else:
            dissprove(disapprvpm.chat_id)
            aname = await disapprvpm.client.get_entity(disapprvpm.chat_id)
            name0 = str(aname.first_name)

        await disapprvpm.edit(
            f"[{name0}](tg://user?id={disapprvpm.chat_id}) `Nub Nimba disapproved to PM KEK!`"
            )
        await asyncio.sleep(2)
        await disapprvpm.delete()
        if LOGGER:
            await disapprvpm.client.send_message(
                LOGGER_GROUP,
                f"[{name0}](tg://user?id={disapprvpm.chat_id})"
                " was disapproved to PM you.",
            )


@register(outgoing=True, pattern="^.block$")
async def blockpm(block):
    """ For .block command, block people from PMing you! """
    if not block.text[0].isalpha() and block.text[0] not in ("/", "#", "@", "!"):

        await block.edit("`You've been blocked Boi!. Now cry in corner`")

        if block.reply_to_msg_id:
            reply = await block.get_reply_message()
            replied_user = await block.client(GetFullUserRequest(reply.from_id))
            aname = replied_user.user.id
            name0 = str(replied_user.user.first_name)
            await block.client(BlockRequest(replied_user.user.id))
            uid = replied_user.user.id
        else:
            await block.client(BlockRequest(block.chat_id))
            aname = await block.client.get_entity(block.chat_id)
            name0 = str(aname.first_name)
            uid = block.chat_id

        try:
            from userbot.modules.sql_helper.pm_permit_sql import dissprove
            dissprove(uid)
        except AttributeError:  # Non-SQL mode.
            pass

        if LOGGER:
            await block.client.send_message(
                LOGGER_GROUP,
                "#BLOCKED\n"
                + "User: " + f"[{name0}](tg://user?id={uid})",
            )


@register(outgoing=True, pattern="^.unblock$")
async def unblockpm(unblock):
    """ For .unblock command, let people PMing you again! """
    if not unblock.text[0].isalpha() and unblock.text[0] \
            not in ("/", "#", "@", "!") and unblock.reply_to_msg_id:

        await unblock.edit("`You have been unblocked.OK NOW GIB MONI`")

        if unblock.reply_to_msg_id:
            reply = await unblock.get_reply_message()
            replied_user = await unblock.client(GetFullUserRequest(reply.from_id))
            name0 = str(replied_user.user.first_name)
            await unblock.client(UnblockRequest(replied_user.user.id))

        if LOGGER:
            await unblock.client.send_message(
                LOGGER_GROUP,
                f"[{name0}](tg://user?id={replied_user.user.id})"
                " was unblocked!.",
            )

CMD_HELP.update({
    "pmpermit": "\
.pm\
\nUsage: Approves the mentioned/replied person to PM.\
\n\n.disapprove\
\nUsage: Disapproves the mentioned/replied person to PM.\
\n\n.block\
\nUsage: Blocks the person.\
\n\n.unblock\
\nUsage: Unblocks the person so they can PM you.\
\n\n.notifoff\
\nUsage: Clears/Disables any notifications of unapproved PMs.\
\n\n.notifon\
\nUsage: Allows notifications for unapproved PMs."
})
