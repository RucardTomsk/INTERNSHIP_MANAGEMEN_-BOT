from telebot import types

keyboard_student = [types.InlineKeyboardButton(text="Документы", callback_data="1")
					,types.InlineKeyboardButton(text="Информация", callback_data="2")
					]

keyboard_kur = [types.InlineKeyboardButton(text="Запрос",callback_data="3")
			,types.InlineKeyboardButton(text="Студенты",callback_data="4")
			]

keyboard_dec = [types.InlineKeyboardButton(text="Запрос",callback_data="3")
			,types.InlineKeyboardButton(text="Студенты",callback_data="5")
			,types.InlineKeyboardButton(text="Кураторы", callback_data="6")
			,types.InlineKeyboardButton(text="Компании",callback_data="7")
			,types.InlineKeyboardButton(text="Опросы",callback_data="8")
			]

keyboard_kom = [types.InlineKeyboardButton(text="Запрос",callback_data="3")
			,types.InlineKeyboardButton(text="Студенты", callback_data="9")
			,types.InlineKeyboardButton(text="Информация", callback_data="10")
			,types.InlineKeyboardButton(text="Опросы", callback_data="11")
]


def build_a_menu_by_roles(mas):
	keyboard = types.InlineKeyboardMarkup(row_width=1)

	mas_button = []
	for i in mas:
		if i == 1:
			for g in keyboard_student:
				mas_button.append(g)
		if i == 2:
			if len(mas) > 1:
				if mas[1] == 3:
					new_keyboard = keyboard_kur
					new_keyboard[1] = types.InlineKeyboardButton(text="Студенты-Куратора",callback_data="4")
					for g in new_keyboard:
						mas_button.append(g)
			else:
				for g in keyboard_kur:
					mas_button.append(g)
		if i == 3:
			if mas[0] == 2:
				new_keyboard = []
				for g in range(1,len(keyboard_dec)):
					if g != 1:
						new_keyboard.append(keyboard_dec[g])
					else:
						new_keyboard.append(types.InlineKeyboardButton(text="Студенты-Деканата",callback_data="5"))
				for g in new_keyboard:
					mas_button.append(g)
			else:
				for g in keyboard_dec:
					mas_button.append(g)
		if i == 4:
			if len(mas) > 1:
				for g in range(1,len(keyboard_kom)):
					mas_button.append(keyboard_kom[g])
			else:
				for g in keyboard_kom:
					mas_button.append(g)

	mas_button.append(types.InlineKeyboardButton(text="Удалить аккаунт", callback_data="delete"))

	print(mas_button)

	for i in mas_button:
		keyboard.add(i)

	return keyboard