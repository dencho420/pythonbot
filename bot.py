import telebot
from telebot import types
import config


bot = config.bot
day = config.day
date = config.date

@bot.message_handler(commands = ['start'])
def start(message):
  keyboard = types.ReplyKeyboardMarkup(row_width=3)
  button1 = types.KeyboardButton('Закрыть смену')
  keyboard.add(button1)
  bot.reply_to(message.chat.id, 'Привет, работничек.', reply_markup=keyboard)

@bot.message_handler(content_types=['text'])
def handle_mes(message):
  if message.text == 'Закрыть смену':
    bot.reply_to(message, f'Отлично, {day(date)} off. Пришли мне данные из 48, выручку.')


bot.polling()