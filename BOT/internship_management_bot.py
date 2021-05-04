import telebot
import config
from telebot import types   #python MySQL
import pymysql
from time import sleep
import threading
from bd_connect import bd_connect
import user_control
import reg_control
import craft_keyboard

db_cur = bd_connect()

bot = telebot.TeleBot(config.API_TELEGRAM_TOKEN)

#Редактор меню, изминение меню по мере работы
def return_menu(call,text_t,build):
	bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=text_t)
	bot.edit_message_reply_markup(chat_id = call.message.chat.id, message_id = call.message.message_id, reply_markup = build)
	pass
	
@bot.message_handler(commands=['start'])
def start_messages(message):
	if(user_control.check_user(message,db_cur)):
		keyboard = types.InlineKeyboardMarkup()
		button = types.InlineKeyboardButton(text="Меню", callback_data="menu")
		keyboard.add(button)
		bot.send_message(message.chat.id,"-----",reply_markup=keyboard)
	
	else:
		bot.send_message(message.chat.id,"Добро пожаловать!!! \n Поскольку мы вас видем впервый раз, введите КОД доступа")
		bot.register_next_step_handler(message,reg_control.check_codes,db_cur,bot)
	pass

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
	if call.data == "menu":
		mas = user_control.return_role(call,db_cur)
		return_menu(call,"Главное меню",craft_keyboard.build_a_menu_by_roles(mas))
		pass
	pass

if __name__ == '__main__':
	bot.infinity_polling()