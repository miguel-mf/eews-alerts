#!/usr/bin/python
import psycopg2
from config import config
import time
import telebot
import math
from tokenID import *
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from tinydb import TinyDB, Query

bot = telebot.TeleBot(telegram_token_eew_santiago_bot)
db = TinyDB('db.json')

@bot.message_handler(commands=['info'])
def handle_command(message):
    bot.reply_to(message, "Este bot te permite recibir alertas rápidas de los sismos que ocurren en Chile, las que puedes personalizar a tu gusto.\n\nPara empezar a recibir alertas personalizadas de terremotos utiliza el comando '/suscribirse' y sigue las instrucciones.\n\nSi deseas recibir todas las alertas disponibles puedes usar el comando /canal para unirte al canal que contiene todas las alertas de sismos en Chile.\n\nPara mayor información sobre los comandos disponibles utiliza el comando '/comandos'.\n\nPara conocer el detalle de como funciona este bot utiliza el comando /teoria.")

@bot.message_handler(commands=['start'])
def handle_command(message):
    bot.reply_to(message, "Este bot te permite recibir alertas rápidas de los sismos que ocurren en Chile, las que puedes personalizar a tu gusto.\n\nPara empezar a recibir alertas personalizadas de terremotos utiliza el comando '/suscribirse' y sigue las instrucciones.\n\nSi deseas recibir todas las alertas disponibles puedes usar el comando /canal para unirte al canal que contiene todas las alertas de sismos en Chile.\n\nPara mayor información sobre los comandos disponibles utiliza el comando '/comandos'.\n\nPara conocer el detalle de como funciona este bot utiliza el comando /teoria.")

@bot.message_handler(commands=['comandos'])
def handle_command(message):
    bot.reply_to(message, "Los comandos disponibles para este bot son los siguientes: \n/comandos - Listado de comandos del bot \n/info - Información general del bot \n/suscribirse - Suscribirte a las alertas de terremotos.\n/desuscribirse - Para dejar de recibir alertas.\n/magnitud - Para definir la magnitud a partir de la cual quieres recibir alertas.\n/ubicacion - Indícanos donde vives para darte alertas más personalizadas.\n/distancia - Para definir la distancia hasta la cual quieres recibir alertas.\n/canal - Recibe una invitación al canal con todas las alertas emitidas a lo largo de Chile.\n/teoria - Para un pequeño resumen del funcionamiento de este bot.\n/contacto - Para enviar tu feedback.")

@bot.message_handler(commands=['suscribirse'])
def handle_command(message):
	if not db.search(user_check.chat_id == message.chat.id):
		bot.reply_to(message, "Ya estás suscrito a estas alertas.")
	else:
		db.insert({'chat_id':message.chat.id, 'magnitud':3.0,'ubicacion':'Ninguna', 'distancia':999999, 'date':message.date, 
					'username':message.from_user.id, 'username':message.from_user.first_name, 'bot'=message.from_user.is_bot})
		bot.reply_to(message, "Felicidades, has sido suscrito a las alertas de terremotos en Chile. Este proceso puede tardar un par de horas en tomar efecto.\n\nRecibirás una notificación por este chat cada vez que ocurra un sismo de magnitud preliminar superior a 3.0 en Chile.\n\nPara personalizar las notificaciones que recibes utiliza los comandos /magnitud, /ubicacion y /distancia.\n\nPara dejar de recibir notificaciones utiliza el comando /desuscribirse.")

@bot.message_handler(commands=['desuscribirse'])
def handle_command(message):
    bot.reply_to(message, "Ya no recibirás notificaciones por este medio. Este proceso puede tardar un par de horas en tomar efecto. \n\nGracias por participar de este proceso.")
		 
@bot.message_handler(commands=['magnitud'])
def handle_command(message):
    bot.reply_to(message, "¿Desde que valor de magnitud preliminar te gustaría recibir notificaciones?\n\nSelecciona un valor entre las siguientes opciones (valor por defecto 3.0)\n\nRecuerda que la magnitud preliminar es una estimación rápida y puede variar con respecto al valor final.", reply_markup=gen_markup_mag())

@bot.message_handler(commands=['ubicacion'])
def handle_command(message):
    bot.reply_to(message, "Selecciona una de las siguientes localidades para establecer tu ubicación y poder obtener alertas para los sismos más cercanos. \n\nCombínalo con el comando /distancia y podrás personalizar los sismos que recibes (Por defecto recibirás notificaciones para todo el territorio chileno).\n\nRecuerda que la ubicación preliminar de los sismos puede contener errores y esto puede afectar las alertas que recibas.\n\nTu ubicación real no será adquirida o utilizada por este sistema de alertas.", reply_markup=gen_markup_regiones())
		 
@bot.message_handler(commands=['distancia'])
def handle_command(message):
    bot.reply_to(message, "Define una distancia máxima hasta la cual recibir alertas.\n\nUtiliza este valor en conjunto con tu /ubicacion para personalizar tus alertas (Por defecto recibirás notificaciones para cualquier distancia).\n\nRecuerda que la ubicación preliminar de los sismos puede contener errores y esto puede afectar las alertas que recibas.\n\nTu ubicación real no será adquirida o utilizada por este sistema de alertas.", reply_markup=gen_markup_distancia())
		 
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

	
def gen_markup_mag():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("3.0", callback_data="mag_3.0"),
	       InlineKeyboardButton("3.5", callback_data="mag_3.5"),
               InlineKeyboardButton("4.0", callback_data="mag_4.0"),
               InlineKeyboardButton("4.5", callback_data="mag_4.5"),
               InlineKeyboardButton("5.0", callback_data="mag_5.0"),
               InlineKeyboardButton("5.5", callback_data="mag_5.5"),
               InlineKeyboardButton("6.0", callback_data="mag_6.0"),
               InlineKeyboardButton("6.5", callback_data="mag_6.5"),
               InlineKeyboardButton("7.0", callback_data="mag_7.0"),
               InlineKeyboardButton("7.5", callback_data="mag_7.5"),
               InlineKeyboardButton("Todas", callback_data="mag_Todas"))
    return markup

def gen_markup_distancia():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("100", callback_data="dist_100"),
	       InlineKeyboardButton("200", callback_data="dist_200"),
	       InlineKeyboardButton("300", callback_data="dist_300"),
	       InlineKeyboardButton("500", callback_data="dist_500"),
	       InlineKeyboardButton("800", callback_data="dist_800"),
	       InlineKeyboardButton("1000", callback_data="dist_1000"),
	       InlineKeyboardButton("Todo Chile", callback_data="dist_Todo Chile"))
    return markup

def gen_markup_regiones():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(InlineKeyboardButton("Norte Grande", callback_data="region_norte-grande"),
	       InlineKeyboardButton("Norte Chico", callback_data="region_norte-chico"),
	       InlineKeyboardButton("Central", callback_data="region_central"),
	       InlineKeyboardButton("Sur", callback_data="region_sur"),
	       InlineKeyboardButton("Austral", callback_data="region_austral"))
    return markup

def gen_markup_norte_grande():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("Arica", callback_data="ubicacion_Arica"),
	       InlineKeyboardButton("Putre", callback_data="ubicacion_Putre"),
	       InlineKeyboardButton("Colchane", callback_data="ubicacion_Colchane"),
	       InlineKeyboardButton("Iquique", callback_data="ubicacion_Iquique"),
	       InlineKeyboardButton("Ollagüe", callback_data="ubicacion_Ollagüe"),
	       InlineKeyboardButton("Tocopilla", callback_data="ubicacion_Tocopilla"),
	       InlineKeyboardButton("Calama", callback_data="ubicacion_Calama"),
	       InlineKeyboardButton("San Pedro de Atacama", callback_data="ubicacion_San-Pedro-de-Atacama"),
	       InlineKeyboardButton("Mejillones", callback_data="ubicacion_Mejillones"),
	       InlineKeyboardButton("Antofagasta", callback_data="ubicacion_Antofagasta"),
	       InlineKeyboardButton("Mina Escondida", callback_data="ubicacion_Mina-Escondida"),
	       InlineKeyboardButton("Taltal", callback_data="ubicacion_Taltal"),
	       InlineKeyboardButton("El Salvador", callback_data="ubicacion_El-Salvador"),
	       InlineKeyboardButton("Chañaral", callback_data="ubicacion_Chañaral"))
    return markup

def gen_markup_norte_chico():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("Caldera", callback_data="ubicacion_Caldera"),
	       InlineKeyboardButton("Copiapó", callback_data="ubicacion_Copiapó"),
	       InlineKeyboardButton("Vallenar", callback_data="ubicacion_Vallenar"),
	       InlineKeyboardButton("Huasco", callback_data="ubicacion_Huasco"),
	       InlineKeyboardButton("Coquimbo", callback_data="ubicacion_Coquimbo"),
	       InlineKeyboardButton("Ovalle", callback_data="ubicacion_Ovalle"),
	       InlineKeyboardButton("Combarbalá", callback_data="ubicacion_Combarbalá"),
	       InlineKeyboardButton("Illapel", callback_data="ubicacion_Illapel"),
	       InlineKeyboardButton("Los Vilos", callback_data="ubicacion_Los-Vilos"),
	       InlineKeyboardButton("San Felipe", callback_data="ubicacion_San-Felipe"))
    return markup

def gen_markup_central():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("Valparaíso", callback_data="ubicacion_Valparaíso"),
	       InlineKeyboardButton("Santiago", callback_data="ubicacion_Santiago"),
	       InlineKeyboardButton("San Antonio", callback_data="ubicacion_San-Antonio"),
	       InlineKeyboardButton("Rancagua", callback_data="ubicacion_Rancagua"),
	       InlineKeyboardButton("San Fernando", callback_data="ubicacion_San-Fernando"),
	       InlineKeyboardButton("Pichilemu", callback_data="ubicacion_Pichilemu"),
	       InlineKeyboardButton("Iloca", callback_data="ubicacion_Iloca"),
	       InlineKeyboardButton("Curicó", callback_data="ubicacion_Curicó"),
	       InlineKeyboardButton("Constitución", callback_data="ubicacion_Constitución"),
	       InlineKeyboardButton("Talca", callback_data="ubicacion_Talca"),
	       InlineKeyboardButton("Linares", callback_data="ubicacion_Linares"),
	       InlineKeyboardButton("Cauquenes", callback_data="ubicacion_Cauquenes"),
	       InlineKeyboardButton("Chillán", callback_data="ubicacion_Chillán"),
	       InlineKeyboardButton("Concepción", callback_data="ubicacion_Concepción"))
    return markup

def gen_markup_sur():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("Los Ángeles", callback_data="ubicacion_Los Ángeles"),
	       InlineKeyboardButton("Lebu", callback_data="ubicacion_Lebu"),
	       InlineKeyboardButton("Angol", callback_data="ubicacion_Angol"),
	       InlineKeyboardButton("Tirúa", callback_data="ubicacion_Tirúa"),
	       InlineKeyboardButton("Temuco", callback_data="ubicacion_Temuco"),
	       InlineKeyboardButton("Villarrica", callback_data="ubicacion_Villarrica"),
	       InlineKeyboardButton("Valdivia", callback_data="ubicacion_Valdivia"),
	       InlineKeyboardButton("La Unión", callback_data="ubicacion_La Unión"),
	       InlineKeyboardButton("Puerto Montt", callback_data="ubicacion_Puerto Montt"),
	       InlineKeyboardButton("Osorno", callback_data="ubicacion_Osorno"))
    return markup

def gen_markup_austral():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("Castro", callback_data="ubicacion_Castro"),
	       InlineKeyboardButton("Chaitén", callback_data="ubicacion_Chaitén"),
	       InlineKeyboardButton("La Junta", callback_data="ubicacion_La Junta"),
	       InlineKeyboardButton("Coyhaique", callback_data="ubicacion_Coyhaique"),
	       InlineKeyboardButton("Puerto Aysén", callback_data="ubicacion_Puerto Aysén"),
	       InlineKeyboardButton("Chile Chico", callback_data="ubicacion_Chile Chico"),
	       InlineKeyboardButton("Cochrane", callback_data="ubicacion_Cochrane"),
	       InlineKeyboardButton("Puerto Natales", callback_data="ubicacion_Puerto Natales"),
	       InlineKeyboardButton("Punta Arenas", callback_data="ubicacion_Punta Arenas"),
	       InlineKeyboardButton("Porvenir", callback_data="ubicacion_Porvenir"),
	       InlineKeyboardButton("Puerto Williams", callback_data="ubicacion_Puerto Williams"))
    return markup


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if "mag" in call.data:
        mag = call.data.split("_")[1]
        bot.answer_callback_query(call.id, "Preferencia de magnitud actualizada: %s" % (mag))
        bot.send_message(call.message.chat.id, "Preferencia de magnitud actualizada: %s" % (mag))
    if "dist" in call.data:
        dist = call.data.split("_")[1]
        bot.answer_callback_query(call.id, "Preferencia de distancia actualizada: %s" % (dist))
        bot.send_message(call.message.chat.id, "Preferencia de distancia actualizada: %s" % (dist))
    if "region" in call.data:
        region = call.data.split("_")[1]
        print(region)
        if region == "norte-grande":
            bot.send_message(call.message.chat.id, "Elige entre las siguientes localidades:" , reply_markup=gen_markup_norte_grande())
        elif region == "norte-chico":
            bot.send_message(call.message.chat.id, "Elige entre las siguientes localidades:" , reply_markup=gen_markup_norte_chico())
        elif region == "central":
            bot.send_message(call.message.chat.id, "Elige entre las siguientes localidades:" , reply_markup=gen_markup_central())
        elif region == "sur":
            bot.send_message(call.message.chat.id, "Elige entre las siguientes localidades:" , reply_markup=gen_markup_sur())
        elif region == "austral":
            bot.send_message(call.message.chat.id, "Elige entre las siguientes localidades:" , reply_markup=gen_markup_austral())
    if "ubicacion" in call.data:
        ubicacion = call.data.split("_")[1].replace("-", " ")
        bot.answer_callback_query(call.id, "Preferencia de ubicación actualizada: %s" % (ubicacion))
        bot.send_message(call.message.chat.id, "Preferencia de ubicación actualizada: %s" % (ubicacion))
	 
		
if __name__ == '__main__':
    bot.polling(none_stop=True)
