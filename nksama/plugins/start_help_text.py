




@bot.on_message(filters.command(["start"], ["/", ".", "?"]))
async def start(bot, m: Message):
    buttons = [
        [
            InlineKeyboardButton(
                "Share any thing! 🤝", switch_inline_query_current_chat=""
            ),
            InlineKeyboardButton(
                "Repo 🏁", url="https://github.com/Team-Aasf/How-All-Bot"
            ),
        ]
    ]
    await m.reply_photo(
        random.choice(BOT),
        caption=text.format(m.from_user.first_name),
        reply_markup=InlineKeyboardMarkup(buttons),
    )
