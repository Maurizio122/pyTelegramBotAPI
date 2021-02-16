#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

import telebot

API_TOKEN = '<1640195297:AAG71yRi5eZqjz7h1atvcpi3jLNI1Tka9zA>'

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Ciao, questo bot è usato solo per scambi seri, no perdite tempo!\
""")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):

else : 

    bot.reply_to(message, 'Se vuoi scambiare contatta @AMPISCORA')




bot.polling()
