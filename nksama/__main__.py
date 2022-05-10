
from nksama.config import SUPPORT_CHAT
import asyncio
import logging

import uvloop
from pyrogram import idle

from nksama import aiohttpsession, bot, log
from nksama.utils.dbfunctions import clean_restart_stage

loop = asyncio.get_event_loop()

logging.basicConfig(
    filename="logs.txt",
    level=logging.INFO,
    filemode="a",
    format="%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s",
    datefmt="%H:%M:%S",
)


async def start_bot():
    restart_data = await clean_restart_stage()

    try:
        log.info("Sending Online Status")
        if restart_data:
            await bot.edit_message_caption(
                restart_data["chat_id"],
                restart_data["message_id"],
                "**Restarted Successfully**",
            )

        else:
            img = "https://telegra.ph/file/9983dec7d8c291f227d0c.jpg"
            await bot.send_photo(f"{SUPPORT_CHAT}", img, caption="@WaifuFunBot Was Started!")
    except Exception:
        pass

    await idle()

    await aiohttpsession.close()
    log.info("Stopping clients")
    await bot.stop()
    log.info("Cancelling asyncio tasks")
    for task in asyncio.all_tasks():
        task.cancel()
    log.info("Dead!")


if __name__ == "__main__":
    uvloop.install()
    try:
        try:
            loop.run_until_complete(start_bot())
        except asyncio.exceptions.CancelledError:
            pass
        loop.run_until_complete(asyncio.sleep(3.0))  # task cancel wait
    finally:
        loop.close()
