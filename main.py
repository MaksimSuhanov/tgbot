import telebot
from telebot import types

bot = telebot.TeleBot('6259067405:AAEgUbhxr7D14sqk9cnw5vVljkZRIYgpdtg')

@bot.message_handler(commands=['start'])
def welcome(message):
    # sti = open('static/AnimatedSticker.tgs', 'rb')
    # bot.send_sticker(message.chat.id, sti)
    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item = types.KeyboardButton("😺Факт о котиках")


    markup.add(item)


    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, "
                                      "бот созданный, чтобы быть подопытным котиком.\n"
                                      "Я знаю много важных фактов о котах.".format(message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)

# @bot.message_handler(commands=['start'])
# def welcome(message):
# 	bot.send_photo(message.chat.id,
#                    photo='https://mobimg.b-cdn.net/v3/fetch/36/365f36a8661229698b3b3a076cc89741.jpeg?w=1470&r=0.5625',
#                    caption='It works!')
#
#
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     item1 = types.KeyboardButton("😺Факт о котиках")
#     item2 = types.KeyboardButton("🦈Факт об акулах")
#     item3 = types.KeyboardButton("😀Как дела?")
#
#     markup.add(item1, item2, item3)
    # markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # item = types.KeyboardButton("Age")
    # markup.add(item)
    # sti = open('static/sticker.tgs', 'rb')
    # bot.send_sticker(message.chat.id, sti)

# @bot.message_handler(content_types=['text'])
# def get_text_messages(message):
#
#     if message.text == "Привет":
#         bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
#     elif message.text == "/help":
#         bot.send_message(message.from_user.id, "Напиши привет")
#     else:
#         bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

# bot.polling(none_stop=True, interval=0)

name = ''
surname = ''
age = 0
@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/reg':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item = types.KeyboardButton('Age')
        markup.add(item)
        bot.send_message(message.from_user.id, "Как тебя зовут?")
        bot.register_next_step_handler(message, get_name) #следующий шаг – функция get_name
    else:
        bot.send_message(message.from_user.id, 'Напиши /reg')

def get_name(message): #получаем фамилию
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'Какая у тебя фамилия?')
    bot.register_next_step_handler(message, get_surname)

def get_surname(message):
    global surname
    surname = message.text
    bot.send_message(message.from_user.id, 'Сколько тебе лет?')
    bot.register_next_step_handler(message, get_age)


def get_age(message):
    global age
    while age == 0: #проверяем что возраст изменился
        try:
             age = int(message.text) #проверяем, что возраст введен корректно
        except Exception:
             bot.send_message(message.from_user.id, 'Цифрами, пожалуйста')
             keyboard = types.InlineKeyboardMarkup() #наша клавиатура
             key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes') #кнопка «Да»
             keyboard.add(key_yes) #добавляем кнопку в клавиатуру
             key_no= types.InlineKeyboardButton(text='Нет', callback_data='no')
             keyboard.add(key_no)
             question = 'Тебе '+str(age)+' лет, тебя зовут '+name+' '+surname+'?'
             bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)

# def get_age(message):
#     global age
#     while age == 0:  # проверяем что возраст изменился
#         try:
#             age = int(message.text)  # проверяем, что возраст введен корректно
#         except Exception:
#             bot.send_message(message.from_user.id, 'Цифрами, пожалуйста')
#         bot.send_message(message.from_user.id,
#                          'Тебе ' + str(age) + ' лет, тебя зовут ' + name + ' ' + surname + '?')
#
#     @bot.callback_query_handler(func=lambda call: True)
#     def callback_worker(call):
#         if call.data == "yes":  # call.data это callback_data, которую мы указали при объявлении кнопки
#          # код сохранения данных, или их обработки
#             bot.send_message(call.message.chat.id, 'Запомню : )')
#         elif call.data == "no":
#             ...  # переспрашиваем


bot.polling(none_stop=True)
