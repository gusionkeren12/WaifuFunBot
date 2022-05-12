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
Hello! Dear Users
I'm An Anime themed Smart VegetaRobot make your group's joyful bellow Using /help commands!!

Powerd by @PegaBots

"""



@bot.on_inline_query()
async def inline_query_handler(client, query):
    string = query.query.lower()
    if string == "":
        await client.answer_inline_query(
            query.id,
            results=[
               InlineQueryResultArticle(
                    input_message_content=InputTextMessageContent(
                        text, disable_web_page_preview=True
                    ),
                    thumb_url="https://telegra.ph/file/32075ee5edfd88e99f6c3.jpg",
                    title=f"🤝 Help",
                    description=f" 😎 About @VegetaRobot",
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
