import telebot
import pymysql
from time import sleep
from telebot import types


def select_code(message,db_cur):
	Z = "SELECT idCodes FROM codes"
	db_cur[1].execute(Z)
	sleep(0.1)
	list_codes = db_cur[1].fetchall()
	mas_codes = []
	for i in list_codes:
		mas_codes.append(str(i[0]))

	return mas_codes
	pass

def check_codes(message,db_cur,bot):
	print(message.text)
	print(select_code(message,db_cur))
	if message.text in select_code(message,db_cur):
		Z = "SELECT Role FROM codes WHERE idCodes=" + message.text
		db_cur[1].execute(Z)
		sleep(0.1)
		Z = "INSERT INTO user (idTG, Role) VALUES (" + str(message.from_user.id) +","+ str(db_cur[1].fetchall()[0][0]) + ")" 
		db_cur[1].execute(Z)
		sleep(0.1)
		db_cur[0].commit()
		bot.send_message(message.chat.id,"Код введен верно!\nВаш ID сохранен и роль выдана")
		keyboard = types.InlineKeyboardMarkup()
		button = types.InlineKeyboardButton(text="Меню", callback_data="menu")
		keyboard.add(button)
		bot.send_message(message.chat.id,"-----",reply_markup=keyboard)
	else:
		bot.send_message(message.chat.id,"Код введен неверно!\nПопробуйте еще раз")
		bot.register_next_step_handler(message,check_codes,db_cur,bot)
	


	

