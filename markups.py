from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

Menyu = KeyboardButton('Ortga qaytish')

#main Menu

item1 = KeyboardButton('Diplom')
item2 = KeyboardButton('Maqola')
item3 = KeyboardButton('Talabalar')
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(item1, item2, item3)

#Kafedra Button

item4 = KeyboardButton('Fizika')
item5 = KeyboardButton('Matematika')
item6 = KeyboardButton('Iqtisod')
item7 = KeyboardButton('Tarix')
Kafedra = ReplyKeyboardMarkup(resize_keyboard=True).add(item4, item5, item6, item7, Menyu)

#Fakultet Button

item8 = KeyboardButton("Fizika-Texnika")
item9 = KeyboardButton("Matmatika-Informatika")
item10 = KeyboardButton("Iqtisodiyot")
item11 = KeyboardButton("Tarix-fakulteti")
Fakultet = ReplyKeyboardMarkup(resize_keyboard=True).add(item8, item9, item10, item11, Menyu)


#Kafedra2 Button

item12 = KeyboardButton("Fizika1")
item13 = KeyboardButton("Matematika1")
item14 = KeyboardButton("Iqtisod1")
item15 = KeyboardButton("Tarix1")
Kafedra2 = ReplyKeyboardMarkup(resize_keyboard=True).add(item12, item13, item14, item15, Menyu)





