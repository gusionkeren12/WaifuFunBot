from pyrogram import filters
import random 
from pyrogram.types import Message
from pyrogram.types.bots_and_keyboards.inline_keyboard_button import InlineKeyboardButton
from pyrogram.types.bots_and_keyboards.inline_keyboard_markup import InlineKeyboardMarkup
from nksama import bot, SUPPORT_CHAT

BOT_IMG = [ "https://telegra.ph/file/b3fbf990e0b67ede241a3.jpg",
           "https://telegra.ph/file/94865dae2576a2fa52732.jpg" ]
text = """
Hello! Dear {}

I'm An Anime themed Smart VegetaRobot make your group's joyful bellow Using /help commands!!

Powerd by @PegaBots
"""


@bot.on_message(filters.command(["start"], ["/", ".", "?"]))
async def start(_, m: Message):
    buttons = [
        [
            InlineKeyboardButton(
                "ADD ME", url="t.me/VegetaRobot?startgroup=true"),
            InlineKeyboardButton(
                "Support", url="t.me/Vegetasupport"),]]

    await m.reply_photo(
        random.choice(BOT_IMG),
        caption=text.format(m.from_user.first_name),
        reply_markup=InlineKeyboardMarkup(buttons),
    )
