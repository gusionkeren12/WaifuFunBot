from pyrogram import filters
from pyrogram.types import Message
from pyrogram.types.bots_and_keyboards.inline_keyboard_button import InlineKeyboardButton
from pyrogram.types.bots_and_keyboards.inline_keyboard_markup import InlineKeyboardMarkup
from nksama import bot



@bot.on_message(filters.command(["start"], ["/", ".", "?"]))
async def start(bot, m: Message):
    buttons = [
        [
            InlineKeyboardButton(
                "ADD ME", switch_inline_query_current_chat=""
            ),
            InlineKeyboardButton(
                "Support", url=f"{SUPPORT_CHAT}"
            ),
        ]
    ]
    await m.reply_photo(
        random.choice(BOT_IMG),
        caption=text.format(m.from_user.first_name),
        reply_markup=InlineKeyboardMarkup(buttons),
    )
