import telebot
from telebot import types
import sqlite3
from datetime import datetime

bot = telebot.TeleBot('token')
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
        return 'вторник'
    elif x == 3:
        return 'среда'
    elif x == 4:
        return 'четверг'
