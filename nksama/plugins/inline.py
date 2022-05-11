import random

from nksama import bot as pbot
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InputTextMessageContent,
    InlineQueryResultArticle,
    InlineQueryResultPhoto,
)

text = """
<b> Information Of bot: </b> /n <b> @VegetaRobot Is A Groupmanager Anime Themed Bot</b>
<b>💬 Bot commands list you want to see send Bot pm `/start` then it will send 🛠 grouptools, 💕 anime buttons [click to read] telegraph method!! </b>
<b> created by @ctzfamily 💫 </b>
"""




@pbot.on_inline_query()
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
