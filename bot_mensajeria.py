#!/usr/bin/python
import psycopg2
from config import config
import time
import telegram
import math
from tokenID import *

bot = telegram.Bot(token=telegram_token_eew_santiago_bot)

#@bot.message_handler(commands=['info'])
#def handle_command(message):
#    bot.reply_to(message, "")

# handle all messages, echo response back to users
@bot.message_handler(func=lambda message: True)
def handle_all_message(message):
	bot.reply_to(message, "Hola, bienvenido al bot de Alerta Temprana. Si buscas información respecto a este bot utiliza el comando /info.")

if __name__ == '__main__':
    bot.polling()
