

bot .on_message(filters.command('hi'))
def hi(_,message):
  message.reply('hi')
