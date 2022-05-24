from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hey {}

Welcome to {}

You can use me to manage channels with tons of features. Use below buttons to learn more !

By @ImDark_Empire
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton(text="🏛️ Return Home 🏛️", callback_data="home")],
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("🤖 Bot Status and More Bots 🤖", url="https://t.me/SLBotOfficial/28")],
        [
            InlineKeyboardButton("How to Use ❔", callback_data="help"),
            InlineKeyboardButton("♾️ About ♾️", callback_data="about")
        ],
        [InlineKeyboardButton("♥ More Amazing bots ♥", url="https://t.me/SLBotOfficial/28")],
        [InlineKeyboardButton("🛫 Support Group 🛫", url="https://t.me/trtechguide")],
    ]

    # Help Message
    HELP = """
Everything is self explanatory after you add a channel.
To add a channel use keyboard button 'Add Channels' or alternatively for ease, use `/add` command

🤖 **Available Commands** 🤖

/about - About The Bot
/help - This Message
/start - Start the Bot

Alternative Commands
/channels - List added Channels
/add - Add a channel
/report - Report a Problem
    """

    # About Message
    ABOUT = """
**About This Bot** 

A telegram channel automation bot by @SLBotOfficial

Source Code : [Click Here](https://github.com/DARKEMPIRESL/ChannelBot)

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Developer : @ImDark_Empire
    """
