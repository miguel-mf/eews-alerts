#!/usr/bin/python
import psycopg2
from config import config
import time
import telegram
import math
from utilidad import *
from tokenID import *

bot = telegram.Bot(token=telegram_token_eew_santiago_bot)

def connect():
    t_anterior = 0
    t = time.time()-10
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    cur = conn.cursor()
    while True:
        cur.execute('SELECT lon,lat,mag,time,modtime from epic.e2event where first_alert = true and modtime > %s order by modtime desc limit 1;' % (t))
        query = cur.fetchone()
        if not query:
            time.sleep(1.0)
            continue
        else:
            lon,lat,mag,ev_time,modtime = query
            t = modtime
            if mag >= 3.0:
                ev_date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(ev_time))
                localidad_cer = localidad_cercana(lat,lon)
                status_msg = "Sismo con magnitud preliminar %.1f detectado. Origen %s (%.1f,%.1f) a las %s" % (mag,localidad_cer,lat,lon,ev_date)
                if ev_time - t_anterior <= 60.0:
                    status_msg = status_msg +" [ALERTA POSIBLEMENTE REPETIDA ASOCIADA AL EVENTO ANTERIOR]"
                t_anterior = ev_time
                status = bot.send_message(chat_id=eew_channel_id, text=status_msg, parse_mode=telegram.ParseMode.HTML)
                status = bot.sendLocation(chat_id=eew_channel_id, latitude=lat, longitude=lon, disable_notification = True)
                status = bot.send_message(chat_id=test_channel_id, text=status_msg, parse_mode=telegram.ParseMode.HTML)
                status = bot.sendLocation(chat_id=test_channel_id, latitude=lat, longitude=lon, disable_notification = True)
                if mag >= 5.0:
                    status = bot.send_message(chat_id=eew_channel_M5_id, text=status_msg, parse_mode=telegram.ParseMode.HTML)
                    status = bot.sendLocation(chat_id=eew_channel_M5_id, latitude=lat, longitude=lon, disable_notification = True)
            else:
                continue

if __name__ == '__main__':
    connect()
