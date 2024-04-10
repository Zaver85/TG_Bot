import telebot
from telebot import types
import random
import time

token = 'YOUR TOKEN'
bot = telebot.TeleBot(token)

links = ['https://t.me/habr_com', 'https://t.me/encryptedch', 'https://t.me/technodrifters', 'https://t.me/startapnaya',
         'https://t.me/tbite', 'https://t.me/anastasiya_krrr1', 'https://t.me/vladamiravi', 'https://t.me/nellifornication_official',
         'https://t.me/xarista', 'https://t.me/mogilkomarina', 'https://t.me/NiktomiusBlack']

@bot.message_handler(commands=['start'])
def send_start(message):
    time.sleep(1)  # Добавляем паузу в 1 секунду
    random_link = random.choice(links)
    reply_markup = types.InlineKeyboardMarkup()
    reply_markup.add(types.InlineKeyboardButton(text="НАЖМИ МЕНЯ", url=random_link))
    bot.send_message(message.chat.id, "Привет! Я развлекательный бот. Нажми на кнопку, чтобы перейти на случайный канал из списка.", reply_markup=reply_markup)

bot.polling()