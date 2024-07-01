
from django.conf import settings
from telebot.async_telebot import AsyncTeleBot

bot = AsyncTeleBot(settings.BOT_TOKEN, parse_mode='HTML')


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
async def send_welcome(message):
    text = 'Hi, I am ReminderBot'
    await bot.reply_to(message, text)


# Handle all other messages with content_type 'text'
# (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
async def echo_message(message):
    await bot.reply_to(message, message.text)
