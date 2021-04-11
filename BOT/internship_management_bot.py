import telebot
import config
from telebot import types   #python MySQL
import pymysql
from time import sleep
import threading
from bd_connect import bd_connect
import user_control
import reg_control

db_cur = bd_connect()

bot = telebot.TeleBot(config.API_TELEGRAM_TOKEN)
	
@bot.message_handler(commands=['start'])
def start_messages(message):
	if(user_control.check_user(message,db_cur)):
		print("OK")
	else:
		bot.send_message(message.chat.id,"Добро пожаловать!!! \n Поскольку мы вас видем впервый раз, введите КОД доступа")
		bot.register_next_step_handler(message,reg_control.check_codes,db_cur,bot)
	pass


if __name__ == '__main__':
	bot.infinity_polling()