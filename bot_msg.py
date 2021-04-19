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
    bot.reply_to(message, "Este bot te permite recibir alertas rápidas de los sismos que ocurren en Chile, las que puedes personalizar a tu gusto.\nPara empezar a recibir alertas personalizadas de terremotos utiliza el comando '/suscribirse' y sigue las instrucciones.\nSi deseas recibir todas las alertas disponibles puedes usar el comando /canal para unirte al canal que contiene todas las alertas de sismos en Chile.\nPara mayor información sobre los comandos disponibles utiliza el comando '/comandos'.\nPara conocer el detalle de como funciona este bot utiliza el comando /teoria.")


@bot.message_handler(commands=['comandos'])
def handle_command(message):
    bot.reply_to(message, "Los comandos disponibles para este bot son los siguientes: \n/comandos - Listado de comandos del bot \n/info - Información general del bot \n/suscribirse - Suscribirte a las alertas de terremotos.\n/desuscribirse - Para dejar de recibir alertas.\n/magnitud - Para definir la magnitud a partir de la cual quieres recibir alertas.\n/ubicacion - Indícanos donde vives para darte alertas más personalizadas.\n/distancia - Para definir la distancia hasta la cual quieres recibir alertas.\n/canal - Recibe una invitación al canal con todas las alertas emitidas a lo largo de Chile.\n/teoria - Para un pequeño resumen del funcionamiento de este bot.\n/contacto - Para enviar tu feedback.")

@bot.message_handler(commands=['suscribirse'])
def handle_command(message):
    bot.reply_to(message, "Felicidades, has sido suscrito a las alertas de terremotos en Chile. Este proceso puede tardar un par de horas en tomar efecto.\nRecibirás una notificación por este chat cada vez que ocurra un sismo de magnitud preliminar superior a 3.0 en Chile.\nPara personalizar las notificaciones que recibes utiliza los comandos /magnitud, /ubicacion y /distancia.\nPara dejar de recibir notificaciones utiliza el comando /desuscribirse.")

@bot.message_handler(commands=['desuscribirse'])
def handle_command(message):
    bot.reply_to(message, "Ya no recibirás notificaciones por este medio. Este proceso puede tardar un par de horas en tomar efecto. Gracias por participar de este proceso.")
		 
@bot.message_handler(commands=['magnitud '])
def handle_command(message):
    bot.reply_to(message, "¿Desde que valor de magnitud preliminar te gustaría recibir notificaciones? Selecciona un valor entre las siguientes opciones (valor por defecto 3.0) 3.0 3.5 4.0 4.5 5.0 5.5 6.0 6.5 7.0 7.5 Recuerda que la magnitud preliminar es una estimación rápida y puede variar con respecto al valor final.")
		 
@bot.message_handler(commands=['ubicacion'])
def handle_command(message):
    bot.reply_to(message, "Selecciona una de las siguientes localidades para establecer tu ubicación y poder obtener alertas para los sismos más cercanos. Combínalo con el comando /distancia y podrás personalizar los sismos que recibes. (Por defecto recibirás notificaciones para todo el territorio chileno) \n Listado de localidades ... \nRecuerda que la ubicación preliminar de los sismos puede contener errores y esto puede afectar las alertas que recibas. Tu ubicación real no será adquirida o utilizada por este sistema de alertas.")
		 
@bot.message_handler(commands=['distancia'])
def handle_command(message):
    bot.reply_to(message, "Define una distancia máxima hasta la cual recibir alertas. Utiliza este valor en conjunto con tu /ubicación para personalizar tus alertas (Por defecto recibirás notificaciones para cualquier distancia)\n100km 200km 300km 500km 800km Todo Chile\nRecuerda que la ubicación preliminar de los sismos puede contener errores y esto puede afectar las alertas que recibas. Tu ubicación real no será adquirida o utilizada por este sistema de alertas.")
		 
@bot.message_handler(commands=['canal'])
def handle_command(message):
    bot.reply_to(message, "Recibe una invitación al canal donde se emiten alertas para todo Chile.")
		 
@bot.message_handler(commands=['teoria'])
def handle_command(message):
    bot.reply_to(message, "Trabajo en proceso")
		 
@bot.message_handler(commands=['contacto'])
def handle_command(message):
    bot.reply_to(message, "Trabajo en proceso")
		 
@bot.message_handler(func=lambda message: True)
def handle_all_message(message):
	bot.reply_to(message, "Hola, bienvenido al bot de Alerta Temprana. Si buscas información respecto a este bot utiliza el comando /info.")

if __name__ == '__main__':
    bot.polling()
