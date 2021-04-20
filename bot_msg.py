#!/usr/bin/python
import psycopg2
from config import config
import time
import telebot
import math
from tokenID import *

bot = telebot.TeleBot(telegram_token_eew_santiago_bot)

@bot.message_handler(commands=['info'])
def handle_command(message):
    bot.reply_to(message, "Este bot te permite recibir alertas rápidas de los sismos que ocurren en Chile, las que puedes personalizar a tu gusto.\n\nPara empezar a recibir alertas personalizadas de terremotos utiliza el comando '/suscribirse' y sigue las instrucciones.\n\nSi deseas recibir todas las alertas disponibles puedes usar el comando /canal para unirte al canal que contiene todas las alertas de sismos en Chile.\n\nPara mayor información sobre los comandos disponibles utiliza el comando '/comandos'.\n\nPara conocer el detalle de como funciona este bot utiliza el comando /teoria.")


@bot.message_handler(commands=['comandos'])
def handle_command(message):
    bot.reply_to(message, "Los comandos disponibles para este bot son los siguientes: \n/comandos - Listado de comandos del bot \n/info - Información general del bot \n/suscribirse - Suscribirte a las alertas de terremotos.\n/desuscribirse - Para dejar de recibir alertas.\n/magnitud - Para definir la magnitud a partir de la cual quieres recibir alertas.\n/ubicacion - Indícanos donde vives para darte alertas más personalizadas.\n/distancia - Para definir la distancia hasta la cual quieres recibir alertas.\n/canal - Recibe una invitación al canal con todas las alertas emitidas a lo largo de Chile.\n/teoria - Para un pequeño resumen del funcionamiento de este bot.\n/contacto - Para enviar tu feedback.")

@bot.message_handler(commands=['suscribirse'])
def handle_command(message):
    bot.reply_to(message, "Felicidades, has sido suscrito a las alertas de terremotos en Chile. Este proceso puede tardar un par de horas en tomar efecto.\n\nRecibirás una notificación por este chat cada vez que ocurra un sismo de magnitud preliminar superior a 3.0 en Chile.\n\nPara personalizar las notificaciones que recibes utiliza los comandos /magnitud, /ubicacion y /distancia.\n\nPara dejar de recibir notificaciones utiliza el comando /desuscribirse.")

@bot.message_handler(commands=['desuscribirse'])
def handle_command(message):
    bot.reply_to(message, "Ya no recibirás notificaciones por este medio. Este proceso puede tardar un par de horas en tomar efecto. \n\nGracias por participar de este proceso.")
		 
@bot.message_handler(commands=['magnitud'])
def handle_command(message):
    bot.reply_to(message, "¿Desde que valor de magnitud preliminar te gustaría recibir notificaciones?\n\nSelecciona un valor entre las siguientes opciones (valor por defecto 3.0) \n\n3.0 3.5 4.0 4.5 5.0 5.5 6.0 6.5 7.0 7.5 \n\nRecuerda que la magnitud preliminar es una estimación rápida y puede variar con respecto al valor final.")
		 
@bot.message_handler(commands=['ubicacion'])
def handle_command(message):
    bot.reply_to(message, "Selecciona una de las siguientes localidades para establecer tu ubicación y poder obtener alertas para los sismos más cercanos. \n\nCombínalo con el comando /distancia y podrás personalizar los sismos que recibes (Por defecto recibirás notificaciones para todo el territorio chileno).\n\n Listado de localidades ... \n\nRecuerda que la ubicación preliminar de los sismos puede contener errores y esto puede afectar las alertas que recibas.\n\nTu ubicación real no será adquirida o utilizada por este sistema de alertas.")
		 
@bot.message_handler(commands=['distancia'])
def handle_command(message):
    bot.reply_to(message, "Define una distancia máxima hasta la cual recibir alertas.\n\nUtiliza este valor en conjunto con tu /ubicación para personalizar tus alertas (Por defecto recibirás notificaciones para cualquier distancia).\n\n100km 200km 300km 500km 800km Todo Chile\n\nRecuerda que la ubicación preliminar de los sismos puede contener errores y esto puede afectar las alertas que recibas.\n\nTu ubicación real no será adquirida o utilizada por este sistema de alertas.")
		 
@bot.message_handler(commands=['canal'])
def handle_command(message):
    bot.reply_to(message, "Para acceder al canal de Alerta Temprana clickea el siguiente link.\n\nhttps://t.me/joinchat/V5-olf-vH5w2YmZh\n\nEn este canal se generan alertas para todos los sismos de magnitud 3.0 y superior en el territorio chileno.")
		 
@bot.message_handler(commands=['teoria'])
def handle_command(message):
    bot.reply_to(message, "Trabajo en proceso")
		 
@bot.message_handler(commands=['contacto'])
def handle_command(message):
    bot.reply_to(message, "Cualquier comentario o sugerencia enviarlo a mmedina@csn.uchile.cl")
		 
@bot.message_handler(func=lambda message: True)
def handle_all_message(message):
	bot.reply_to(message, "Hola, bienvenido al bot de Alerta Temprana. Si buscas información respecto a este bot utiliza el comando /info.")

if __name__ == '__main__':
    bot.polling()
