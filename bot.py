from telebot import telebot



@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, 'Hello! This is a simple bot that responds to /start command.')