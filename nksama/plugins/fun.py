from pyrogram.types import Message
from pyrogram import filters

@bot.on_message(filters.command('hmeme'))
def hmeme(_, m: message):
    reply = m.reply_to_message
    if reply:
        reply.reply_animation(random.choice(deathnote),
                              caption="{} Added Death Note List!".format(m.reply_user.mention)
        
    else:
        m.reply_animation(random.choice(deathnote),
                              caption="{} Added Death Note List!".format(m.from_user.mention)
        
