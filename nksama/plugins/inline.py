import random
from nksama.plugins.dev_user import *

from nksama import bot , SUPPORT_CHAT, UPDATES_CHANNEL
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InputTextMessageContent,
    InlineQueryResultArticle,
    InlineQueryResultPhoto,
)

text = """
Hello! {}
I'm An Anime themed Smart VegetaRobot make your group's joyful bellow Using /help commands!!

✪ Server time : {}
✪ Uptime: {}

Powerd by @PegaBots

"""

start_time = time.time()
    end_time = time.time()
    ping_time = round((end_time - start_time) * 1000, 3)
    uptime = get_readable_time((time.time() - StartTime))


@bot.on_inline_query()
async def inline_query_handler(client, query):
    string = query.query.lower()
    if string == "":
        await client.answer_inline_query(
            query.id,
            results=[
               InlineQueryResultArticle(
                    input_message_content=InputTextMessageContent(
                        text.format(ping_time, uptime), disable_web_page_preview=True
                    ),
                    thumb_url="https://telegra.ph/file/32075ee5edfd88e99f6c3.jpg",
                    title=f"🤝 Help",
                    description=f"how to use @VegetaRobot",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    "Support",
                                    url=f"t.me/{SUPPORT_CHAT}",
                                ),
                               
                                 InlineKeyboardButton(
                                    "Updates",
                                    url=f"t.me/{UPDATES_CHANNEL}",),
                                ],
                                 [
                                     
                                InlineKeyboardButton(
                                    "Share any thing! 🤝", switch_inline_query=""
                                ),
                            ]
                        ]
                    ),
                ),
            ],
        )
