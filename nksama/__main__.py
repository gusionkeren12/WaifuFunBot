from nksama import bot
import logging
import nksama.plugins
from nksama.config import SUPPORT_CHAT


logging.basicConfig(
    filename="logs.txt",
    level=logging.INFO,
    filemode="a",
    format="%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s",
    datefmt="%H:%M:%S",
)

def main():
    bot.run()
    bot.send_message(f"{SUPPORT_CHAT}", "I'm Now online")


if __name__ == "__main__":
    main()
    
    
