import telebot
import pymysql
from time import sleep

def check_user(message,db_cur):
	Z = "SELECT COUNT(idTG) FROM user WHERE idTG =" + str(message.from_user.id)
	db_cur[1].execute(Z)
	sleep(0.1)
	if(int(db_cur[1].fetchall()[0][0]) == 0):
		return False
	else:
		return True
	pass