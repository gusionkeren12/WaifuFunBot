# Komi-San
Telegram Group Management Bot based on Pyrogram

<b> More updates coming soon </b>

[Support Group](https://t.me/Komisan_Support)

<b> Open a Pull request
if you wana contribute </b>


Example for making new plugins

```
from nksama import bot , help_message
from pyrogram import filters

@bot.on_message(filters.command('hi'))
def hi(_,message):
  message.reply('hi')
  


```


# How to deploy ?

__Vars__ :

```
API_ID - my.telegram.org
API_HASH -  my.telegram.org
BOT_TOKEN - @botfather
MONGO_URL

```

<h1>
    <p align="center">
        <a href="https://heroku.com/deploy?template=https://github.com/thehamkercat/WilliamButcherBot">
            <img src="https://www.herokucdn.com/deploy/button.svg" alt="Deploy">
        </a>
    </p>
</h1>
