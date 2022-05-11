from pyrogram.types.bots_and_keyboards.inline_keyboard_button import InlineKeyboardButton
from pyrogram.types.bots_and_keyboards.inline_keyboard_markup import InlineKeyboardMarkup
from nksama import bot
from pyrogram import filters 
from nksama import help_message


@bot.on_message(filters.command('start'))
def start(_,message):

    bot.send_photo(message.chat.id , photo="https://telegra.ph/file/14f6ced5fa87e62b66977.jpg", caption="help and commands!", reply_markup=InlineKeyboardMarkup([ 
        [InlineKeyboardButton('[ help ]' , callback_data="vegeta_admin")]
    ]))
    
    
@bot.on_message(filters.command('id'))
def ids(_,message):
  reply = message.reply_to_message
  if reply:
    message.reply_text(f"**Your id**: {message.from_user.id}\n**User id**: {reply.from_user.id}\n**chat id**: {message.chat.id}")
  else:
    message.reply(f"**Your id**: {message.from_user.id}\n**chat id**: {message.chat.id}")

    
elif query.data == "vegeta_admin":
        query.message.edit_caption(
            "*๏ Let's make your group bit effective now*"
            "\nCongragulations, VegetaRobot now ready to manage your group."
            "\n\n*Admin Tools*"
            "\nBasic Admin tools help you to protect and powerup your group."
            "\nYou can ban members, Kick members, Promote someone as admin through commands of bot."
            "\n\n*Greetings*"
            "\nLets set a welcome message to welcome new users coming to your group."
            "\nsend `/setwelcome [message]` to set a welcome message!",
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton('WoW', url="t.me/vegetarobot")]]
            ),
        )
    
help_message.append({
    "Module_Name": "admin" ,
    "Help": """
/ban - reply to a user
/unban user id or username
/pin - reply to a message
/unpin - reply to a message
"""})  
