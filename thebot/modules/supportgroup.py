"""Emoji
Available Commands:
.support
Credits to noone
"""


import asyncio

from thebot import CMD_HELP
from thebot.utils import friday_on_cmd


@friday.on(friday_on_cmd("friday"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.1
    animation_ttl = range(0, 36)
    # input_str = event.pattern_match.group(1)
    # if input_str == "support":
    await event.edit("for our support group")
    animation_chars = [
        "Click here",
        "[Support Group](https://t.me/FRIDAYSUPPORTOFFICIAL)",
    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 18])


CMD_HELP.update(
    {
        "supportgroup": "**Support Group**\
\n\n**Syntax : **`.friday`\
\n**Usage :** Creates link for ʄʀɨɖǟʏ support group."
    }
)