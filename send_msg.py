import telegram
from tokenID import *


### Input ###
mensaje = "Este es un mensaje de prueba."
mag = 8.0 
lat = -33
lon = -74
#############

def main():
    db = TinyDB('db_users.json')
    user_check = Query()
    bot = telegram.Bot(token=telegram_token_eew_santiago_bot)
    status = bot.send_message(chat_id=eew_channel_id, text=mensaje, parse_mode=telegram.ParseMode.HTML)
    status = bot.send_message(chat_id=test_channel_id, text=mensaje, parse_mode=telegram.ParseMode.HTML)
    if mag >= 5.0:
        status = bot.send_message(chat_id=eew_channel_M5_id, text=mensaje, parse_mode=telegram.ParseMode.HTML)
    distancias = distancia_a_localidades(lat,lon)
    for entry in db.all:
        if entry.ubicacion == 'Ninguna':
            en_rango = True
        else:
            ubicacion = entry.ubicacion
            distancia = distancias.ubicacion
            if distancia <= entry.distancia:
                en_rango = True
            else:
                en_rango = False # Creo que esto es redundante.
                continue
        if (mag >= entry.magnitud) and en_rango:
            status = bot.send_message(chat_id=entry.chat_id, text=mensaje, parse_mode=telegram.ParseMode.HTML)
    
if __name__ == '__main__':
    main()
