import telebot
import psycopg2 
from telebot import types
 
conn = psycopg2.connect( 
    host = "localhost", 
    database = "postgres", 
    user = "postgres",  
    password  = "123456") 
 
cursor = conn.cursor() 

bot = telebot.TeleBot("6933769115:AAEizT969-xkjsupy9D3mLCVUG3CujMjgak")

def is_table_reserved(table_number): 
    cursor.execute("SELECT is_reserved FROM tables WHERE table_number = %s", (table_number,)) 
    result = cursor.fetchone() 
    if result: 
        return result[0] 
    return False 


def is_vip_room_reserved(room_number): 
    cursor.execute("SELECT is_reserved FROM vip_rooms WHERE room_number= %s", (room_number,)) 
    result = cursor.fetchone() 
    if result: 
        return result[0] 
    return False 


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, <b>{message.from_user.first_name}! </b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')

@bot.message_handler(commands=['s'])
def welcome(message):
    chat_id = message.chat.id
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = telebot.types.KeyboardButton(text="Забронировать стол и проверить его доступность")
    button2 = telebot.types.KeyboardButton(text="Забронировать VIP Кабинку")
    button3 = telebot.types.KeyboardButton(text="Отменить бронирование стола")
    button4 = telebot.types.KeyboardButton(text="Отменить бронирование VIP Кабинки")
    keyboard.add(button1, button2)
    keyboard.add(button3, button4)
    bot.send_message(chat_id, 'Добро пожаловать в бота', reply_markup=keyboard)

@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "Забронировать стол и проверить его доступность"):
        bot.send_message(message.chat.id, text="Введите номер стола,который хотите забронировать:")
        bot.register_next_step_handler(message, reserve_table)

    elif(message.text == "Забронировать VIP Кабинку"):
        bot.send_message(message.chat.id, text = 'Введите желаемую кабинку:')
        bot.register_next_step_handler(message, reserve_vip_room)
    elif(message.text == "Отменить бронирование стола"):
        bot.send_message(message.chat.id, text = " Введите стол , на котором хотите отменить бронь")
        bot.register_next_step_handler(message, cancel_table_reservation)
    else:
        (message.text == "Отменить бронирование VIP Кабинки")
        bot.send_message(message.chat.id, text ="Введите номер кабинки , у которой хотите отменить бронирование")
        bot.register_next_step_handler(message, cancel_vip_room_reservation)


def reserve_table(message): 
    if is_table_reserved(message.text): 
        bot.send_message(message.chat.id , text ="Стол уже занят.") 
    else: 
        cursor.execute("UPDATE tables SET is_reserved = TRUE WHERE table_number = %s", (message.text,)) 
        conn.commit() 
        bot.send_message(message.chat.id , text ="Стол забронирован.") 


def reserve_vip_room(message): 
    if is_vip_room_reserved(message.text): 
        bot.send_message(message.chat.id , text ="VIP Кабинка уже занята.") 
    else: 
        cursor.execute("UPDATE vip_rooms SET is_reserved = TRUE WHERE room_number = %s", (message.text)) 
        conn.commit() 
        bot.send_message(message.chat.id , text ="VIP Кабинка забронирована.") 


def cancel_table_reservation(message): 
    if is_table_reserved(message.text): 
        cursor.execute("UPDATE tables SET is_reserved = FALSE WHERE table_number = %s", (message.text)) 
        conn.commit() 
        bot.send_message(message.chat.id , text ="Бронирование стола отменено.") 
    else:
        bot.send_message(message.chat.id , text ="Стол не забронирован. ")


def cancel_vip_room_reservation(message): 
    if is_vip_room_reserved(message.text): 
        cursor.execute("UPDATE vip_rooms SET is_reserved = FALSE WHERE room_number = %s", (message.text)) 
        conn.commit() 
        bot.send_message(message.chat.id , text ="Бронирование VIP кабинки отменено.") 
    else:
        bot.send_message(message.chat.id , text ="VIP кабинка не забронирована")
    

bot.infinity_polling()