import telebot
from telebot import types

token = '...'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, жми - /button')


@bot.message_handler(commands=['button'])
def button_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Мой профиль LinkedIn')
    item2 = types.KeyboardButton('Мой профиль Instagram')
    markup.add(item1)
    markup.add(item2)
    bot.send_message(message.chat.id, 'My Info - выбирай кнопку ниже :-)', reply_markup=markup)


@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text == 'Мой профиль LinkedIn':
        bot.send_message(message.chat.id, 'Заходи в гости - https://www.linkedin.com/in/aliaksandr-linik/')
    elif message.text == 'Мой профиль Instagram':
        bot.send_message(message.chat.id, 'Заходи в гости - https://www.instagram.com/a.linik1986/')


bot.infinity_polling()

