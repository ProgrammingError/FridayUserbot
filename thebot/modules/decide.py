<<<<<<< HEAD:thebot/modules/decide.py
"""Quickly make a decision
Syntax: .decide"""
import requests

from fridaybot import CMD_HELP
from fridaybot.utils import friday_on_cmd


@friday.on(friday_on_cmd("decide"))
async def _(event):
    if event.fwd_from:
        return
    message_id = event.message.id
    if event.reply_to_msg_id:
        message_id = event.reply_to_msg_id
    r = requests.get("https://yesno.wtf/api").json()
    await borg.send_message(
        event.chat_id, r["answer"], reply_to=message_id, file=r["image"]
    )
    await event.delete()


CMD_HELP.update(
    {
        "decide": "**Decide**\
\n\n**Syntax : **`.decide`\
\n**Usage :** Use this plugin to quickly make a decision."
    }
)
=======
"""Quickly make a decision
Syntax: .decide"""
import requests

from thebot import CMD_HELP
from thebot.utils import friday_on_cmd


@friday.on(friday_on_cmd("decide"))
async def _(event):
    if event.fwd_from:
        return
    message_id = event.message.id
    if event.reply_to_msg_id:
        message_id = event.reply_to_msg_id
    r = requests.get("https://yesno.wtf/api").json()
    await borg.send_message(
        event.chat_id, r["answer"], reply_to=message_id, file=r["image"]
    )
    await event.delete()


CMD_HELP.update(
    {
        "decide": "**Decide**\
\n\n**Syntax : **`.decide`\
\n**Usage :** Use this plugin to quickly make a decision."
    }
)
>>>>>>> c1530b7480a7e9f27bd9921a3bdf5024adbc925a:fridaybot/modules/decide.py
