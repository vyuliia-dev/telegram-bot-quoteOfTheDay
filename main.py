import os
from dotenv import load_dotenv
import telebot
from telebot import types
import random

load_dotenv()
bot = telebot.TeleBot(os.getenv("BOT_TOKEN"))


def do_not_none(value):
    if value is None:
        return ' '
    return value


def get_quotes():
    with open('quotes.txt', 'r', encoding='utf-8') as f:
        content = f.read()
        quotes = content.split('===')
        random_quote = random.choice(quotes).strip()
        return random_quote


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Хочу подсказку', callback_data='quote'))
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}! '
                                      f' Здесь ты можешь получить подсказку на день!', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data == 'quote':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Повторить подсказку', callback_data='quote'))
        bot.send_message(call.message.chat.id, get_quotes(), reply_markup=markup)
        bot.answer_callback_query(call.id)


@bot.message_handler(commands=['quote'])
def quote(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Повторить подсказку', callback_data='quote'))
    bot.send_message(message.chat.id, get_quotes(), reply_markup=markup)


bot.polling(none_stop=True)
