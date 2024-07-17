import telebot
from telebot import types
import sqlite3
from datetime import datetime

bot = telebot.TeleBot('7423765828:AAFGDTXhSV9pYPRoJqUj_B7kOcdT0wMPpRk')
db = sqlite3
date = datetime.now()
con = sqlite3.connect("baza")
cursor = con.cursor()

def day(date):
    x = date.weekday()
    if x == 0:
        return 'воскресенье'
    elif x == 1:
        return 'понедельник'
    elif x == 2:
        return 'среда'
    elif x == 3:
        return 'четверг'