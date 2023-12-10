import telebot
import psycopg2 
from telebot import types
 
conn = psycopg2.connect( 
    host = "localhost", 
    database = "fornurs", 
    user = "postgres",  
    password  = "123456") 
 
cursor = conn.cursor() 

bot = telebot.TeleBot("6933769115:AAEizT969-xkjsupy9D3mLCVUG3CujMjgak")

admin_rooms = [6320258945, 5138539806]


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Здравствуйте, <b>{message.from_user.first_name}! </b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')
    chat_id = message.chat.id
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = telebot.types.KeyboardButton(text="Войти в систему как админ")
    button2 = telebot.types.KeyboardButton(text="Войти как обычный пользователь")
    keyboard.add(button1, button2)
    bot.send_message(chat_id, 'Добро пожаловать в бота', reply_markup=keyboard)
    
    
@bot.message_handler()
def func(message):
    chat_id = message.chat.id
    #Производим вход
    if message.text == 'Войти в систему как админ':
    #

        #Добавляем кнопки при входе , как админ
        user_id = message.from_user.id
        if user_id in admin_rooms:
            bot.send_message(message.chat.id, "Вы вошли в систему как администратор.")
            keyboard =types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1 = types.KeyboardButton(text="Забронированные столы")
            button2 = types.KeyboardButton(text="Свободные столы")
            button3 = types.KeyboardButton(text="Свободные vip-кабинки")
            button4 = types.KeyboardButton(text="Занятые vip-кабинки")
            button5 = types.KeyboardButton(text="Отменить бронирование стола")
            button6 = types.KeyboardButton(text="Отменить бронирование vip-кабинки")
            keyboard.add(button1, button2)
            keyboard.add(button3, button4)
            keyboard.add(button5, button6)
            bot.send_message(chat_id, 'Выберите действие', reply_markup=keyboard)
        else:
            bot.send_message(message.chat.id, "Ваш ID не является администраторским.")
        #

            
    #Выбираем ,кем мы являемся
    elif message.text == 'Войти как обычный пользователь':
        bot.send_message(message.chat.id,'Введите ваше имя:')
        bot.register_next_step_handler(message , insert_name)
    #


    #Функция для бронирования стола
    elif message.text == 'Забронировать стол' :
        bot.send_message(message.chat.id, text="Введите номер стола,который хотите забронировать от 1 до 10:")
        bot.register_next_step_handler(message, reserve_table )

    #


    #функция для бронирования вип кабинки
    elif message.text == "Забронировать vip-кабинку" :
        bot.send_message(message.chat.id, text='Введите желаемую кабинку от 1 до 10:')
        bot.register_next_step_handler(message, reserve_vip_room)
    #

        #Проверяем какие столы забронированны
    elif message.text == 'Забронированные столы' and message.from_user.id in admin_rooms :
        cursor.execute("SELECT table_number FROM tables WHERE is_reserved = TRUE")
        reserved_tables = cursor.fetchall()
        if reserved_tables:
            reserved_tables_str = ", ".join(str(table[0]) for table in reserved_tables)
            message_text = f"Занятые столы: {reserved_tables_str}"
        else:
            message_text = "Все столы свободны."
        bot.send_message(message.chat.id, message_text)
        #


        #Проверяем свободные столы
    elif message.text == 'Свободные столы' and message.from_user.id in admin_rooms :
        cursor.execute("SELECT table_number FROM tables WHERE is_reserved = FALSE")
        reserved_tables = cursor.fetchall()
        if reserved_tables:
            reserved_tables_str = ", ".join(str(table[0]) for table in reserved_tables)
            message_text = f"Свободные столы: {reserved_tables_str}"
        else:
            message_text = "Все столы заняты."
        bot.send_message(message.chat.id, message_text)
        #


        #Функция для просмотра свободных vip-кабинок
    elif message.text == 'Свободные vip-кабинки' and message.from_user.id in admin_rooms :
        cursor.execute("SELECT room_number FROM vip_rooms WHERE is_reserved = FALSE")
        reserved_tables = cursor.fetchall()
        if reserved_tables:
            reserved_tables_str = ", ".join(str(table[0]) for table in reserved_tables)
            message_text = f"Свободные кабинки: {reserved_tables_str}"
        else:
            message_text = "Все кабинки заняты."
        bot.send_message(message.chat.id, message_text)
        #


    #функция для просмотра занятых вип кабинок
    elif message.text == 'Занятые vip-кабинки' and message.from_user.id in admin_rooms :
        cursor.execute("SELECT room_number FROM vip_rooms WHERE is_reserved = TRUE")
        reserved_tables = cursor.fetchall()
        if reserved_tables:
            reserved_tables_str = ", ".join(str(table[0]) for table in reserved_tables)
            message_text = f"Занятые vip-кабинки: {reserved_tables_str}"
        else:
            message_text = "Все кабинки свободны."
        bot.send_message(message.chat.id, message_text)
    # 

    #функция для отмены бронирования стола
    elif message.text == 'Отменить бронирование стола' and message.from_user.id in admin_rooms :
        bot.send_message(message.chat.id, 'Введите номер стола')
        bot.register_next_step_handler(message,cancel_table_reservation)
    #


    #Функция для отмены бронирования вип кабинки
    elif message.text == 'Отменить бронирование vip-кабинки' and message.from_user.id in admin_rooms :
        bot.send_message(message.chat.id, 'Введите номер кабинки')
        bot.register_next_step_handler(message,cancel_vip_room_reservation)
    #




#Дополнительные функции
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

def insert_name(message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    username = message.text
    
    # Проверяем, существует ли пользователь уже в базе данных
    cursor.execute("SELECT username FROM users WHERE user_id = %s", (user_id,))
    existing_username = cursor.fetchone()
    
    if existing_username:
        # Обновляем имя пользователя в базе данных
        update_query = 'UPDATE users SET username = %s WHERE user_id = %s'
        cursor.execute(update_query, (username, user_id))
    else:
        # Вставляем новое имя пользователя в базу данных
        insert_query = 'INSERT INTO users (user_id, username) VALUES (%s, %s)'
        cursor.execute(insert_query, (user_id, username,))
    
    conn.commit()
    bot.send_message(message.chat.id, "Имя успешно добавлено в базу данных.")
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton(text="Забронировать стол")
    button2 = types.KeyboardButton(text="Забронировать vip-кабинку")
    keyboard.add(button1, button2)
    bot.send_message(chat_id, 'Пожалуйста выберите следующее действие:', reply_markup=keyboard)

def reserve_table(message):
    table_number = message.text
    if not is_valid_table_number(table_number):
        bot.send_message(message.chat.id, text="Введите корректный номер стола от 1 до 10.")
    elif is_table_reserved(table_number):
        bot.send_message(message.chat.id, text="Стол уже занят.")
    else:
        username = get_username(message.from_user.id)
        if username:
            cursor.execute("UPDATE tables SET is_reserved = TRUE, reserved_by = %s WHERE table_number = %s", (username, message.text))
            conn.commit()
            bot.send_message(message.chat.id, text=f"Стол {message.text} забронирован для пользователя {username}.")
        else:
            bot.send_message(message.chat.id, text="Что-то пошло не так. Пожалуйста, попробуйте еще раз.")

def get_username(user_id):
    cursor.execute("SELECT username FROM users WHERE user_id = %s", (user_id,))
    result = cursor.fetchone()
    return result[0] if result else None

def reserve_vip_room(message):
    room_number = message.text
    if not is_valid_vip_room_number(room_number):
        bot.send_message(message.chat.id, text="Введите корректный номер VIP-кабинки от 1 до 10.")
    elif is_vip_room_reserved(room_number):
        bot.send_message(message.chat.id, text="VIP-кабинка уже занята.")
    else:
        username = get_username(message.from_user.id)
        if username:
            cursor.execute("UPDATE vip_rooms SET is_reserved = TRUE, reserved_by = %s WHERE room_number = %s", (username, message.text))
            conn.commit()
            bot.send_message(message.chat.id, text=f"Кабинка {message.text} забронирована для пользователя {username}.")
        else:
            bot.send_message(message.chat.id, text="Что-то пошло не так. Пожалуйста, попробуйте еще раз.")

def is_valid_table_number(table_number):
    return 1 <= int(table_number) <= 10

def is_valid_vip_room_number(room_number):
    return 1 <= int(room_number) <= 10
    #

bot.infinity_polling()

