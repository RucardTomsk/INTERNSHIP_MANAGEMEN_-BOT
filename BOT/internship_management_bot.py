import config
import telebot
from telebot import types   #python MySQL
import pymysql
from time import sleep
import threading

db = pymysql.connect(
	host=config.HOST,
	database=config.DATABAZA,
	user=config.USER,
	password=config.PASSWORD
	)

cur = db.cursor()

bot = telebot.TeleBot(config.API_TELEGRAM_TOKEN)

def check_user(message):
	Z = "SELECT COUNT(idTG) FROM user WHERE idTG =" + str(message.from_user.id)
	cur.execute(Z)
	sleep(0.1)
	if(int(cur.fetchall()[0][0]) == 0):
		return False
	else:
		return True
	pass

@bot.message_handler(content_types=["text"])
def check_codes(message):
	if message.text != "/start":
		print(message.text)
		Z = "SELECT Role FROM codes WHERE idCodes =" + str(message.text)
		cur.execute(Z)
		role = cur.fetchall()[0][0]
		if(role != ""):
			Z = "INSERT INTO user (idTG, Role) VALUES (" + str(message.from_user.id) + "," + str(role) + ")"
			cur.execute(Z)
			sleep(0.1)
			db.commit()
		else:
			bot.send_message(message.chat.id,"Такого кода доступа нету!!!")
	

@bot.message_handler(commands=['start'])
def start_messages(message):
	if(check_user(message)):
		print("OK")
	else:
		bot.send_message(message.chat.id,"Добро пожаловать!!! \n Поскольку мы вас видем впервый раз, введите КОД доступа")
	pass

if __name__ == '__main__':
	bot.infinity_polling()