from nksama import bot
import asyncio
import logging
from nksama.config import SUPPORT_CHAT


logging.basicConfig(
    filename="logs.txt",
    level=logging.INFO,
    filemode="a",
    format="%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s",
    datefmt="%H:%M:%S",
)

if __name__ == "__main__":
    bot.run()
    
    bot.send_message(f"{SUPPORT_CHAT}" , "@WaifuFunBot Alive!")
    
