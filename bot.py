from telebot import TeleBot, types
import config
import tinkture

bot = config.bot
day = config.day
date = config.date

# Создаем словарь для хранения состояний пользователей
user_states = {}
user_tincture_choices = {}  # Для хранения выбора настойки пользователей

# Определяем состояния
STATE_WAITING_FOR_REVENUE = "waiting_for_revenue"
STATE_WAITING_FOR_VOLUME = "waiting_for_volume"

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton('Закрыть смену', callback_data='close_shift')
    button2 = types.InlineKeyboardButton('Рассчитать настойку', callback_data='choose_tincture')
    keyboard.add(button1, button2)
    bot.reply_to(message, 'Привет, работничек.', reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data == 'close_shift')
def handle_callback_query(call):
    chat_id = call.message.chat.id
    bot.send_message(chat_id, 'Отлично, {} off. Пришли мне данные из 48, выручку.'.format(day(date)))
    user_states[chat_id] = STATE_WAITING_FOR_REVENUE

@bot.callback_query_handler(func=lambda call: call.data == 'choose_tincture')
def handle_tincture_choice(call):
    chat_id = call.message.chat.id
    keyboard = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton('Лимка', callback_data='Лимка')
    button2 = types.InlineKeyboardButton('Тайга', callback_data='Тайга')
    button3 = types.InlineKeyboardButton('Нутелла', callback_data='Нутелла')
    keyboard.add(button1, button2, button3)
    bot.send_message(chat_id, 'Выберите вариант настойки:', reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data in ['Лимка', 'Тайга', 'Нутелла'])
def handle_tincture_variant(call):
    chat_id = call.message.chat.id
    user_tincture_choices[chat_id] = call.data
    bot.send_message(chat_id, 'Введите объем настойки, который хотите приготовить (в литрах).')
    user_states[chat_id] = STATE_WAITING_FOR_VOLUME

@bot.message_handler(content_types=['text'])
def handle_mes(message):
    chat_id = message.chat.id
    if chat_id in user_states and user_states[chat_id] == STATE_WAITING_FOR_REVENUE:
        try:
            revenue = int(message.text)
            # Здесь можно добавить код для сохранения выручки в базу данных
            bot.reply_to(message, 'Спасибо! Выручка {} записана.'.format(revenue))
            user_states.pop(chat_id)  # Сбрасываем состояние пользователя
        except ValueError:
            bot.reply_to(message, 'Пожалуйста, введите числовое значение для выручки.')
    elif chat_id in user_states and user_states[chat_id] == STATE_WAITING_FOR_VOLUME:
        try:
            volume = float(message.text)
            tincture_choice = user_tincture_choices.get(chat_id)
            ingredients = tinkture.calculate_ingredients(volume, tincture_choice)
            reply = f'Для приготовления {volume} литров настойки вам понадобится:\n'
            for ingredient, amount in ingredients.items():
                reply += f'- {ingredient}: {amount} грамм/мл\n'
            bot.reply_to(message, reply)
            user_states.pop(chat_id)  # Сбрасываем состояние пользователя
            user_tincture_choices.pop(chat_id)  # Сбрасываем выбор настойки
        except ValueError:
            bot.reply_to(message, 'Пожалуйста, введите числовое значение для объема.')
    else:
        bot.reply_to(message, 'Пожалуйста, используйте команды или кнопки для взаимодействия с ботом.')

bot.polling(none_stop=True)
