import random
import telebot
from telebot import types

bot = telebot.TeleBot('5187792169:AAGBRBg9APCxSVfdnxSRyiqLFR3lPb3izI0')

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет <u><b>{message.from_user.first_name} {message.from_user.last_name} </b> </u>'
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    info = types.KeyboardButton(f'ℹ️ Информация ℹ️')
    website = types.KeyboardButton(f'🤠 Создатель 🤠')
    commands = types.KeyboardButton('👍🏿 Команды 👍🏿')
    rand = types.KeyboardButton(f"❓ Рандомное число ❓")
    markup.add(info, website, rand, commands)
    bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_user_text(message, random=random):
    if message.chat.type == 'private':
        if message.text == '❓ Рандомное число ❓':
            bot.send_message(message.chat.id, 'Ваше число: ' + str(random.randint(0,10000)))

        elif message.text == 'ℹ️ Информация ℹ️':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            binfo = types.KeyboardButton(f'🤖 О боте 🤖')
            wtf = types.KeyboardButton(f'📦 Что в коробке? 📦')
            back = types.KeyboardButton(f"🔙 Назад 🔙")
            markup.add(binfo, wtf, back)
            bot.send_message(message.chat.id, 'ℹ️ Информация ℹ️', parse_mode='html', reply_markup=markup)
        elif message.text == '👍🏿 Команды 👍🏿':
            bot.send_message(message.chat.id, '/start - меню бота,\nHello - приветствие,\nID - узнать свой ID,\nPhoto - фото бота,\nОтправь любое фото боту, он его оценит.')
        elif message.text == '🤖 О боте 🤖':
            bot.send_message(message.chat.id, 'Этот бот был создан при поддержке \nни-ко-го')
        elif message.text == '📦 Что в коробке? 📦':
            a = ['Нет тут ничего!!📦', 'Тебе повезло, в коробке оказалось 4 копейки', '❌ sheet ❌', "🎉 jackpot - one belarusian rouble 🎊", 'Пустота...', 'Штаны adidaz']
            bot.send_message(message.chat.id, (random.choice(a)))

        elif message.text == '🤠 Создатель 🤠':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            binfo = types.KeyboardButton(f'🤖 VK 🤖')
            wtf = types.KeyboardButton(f'🤠 TG 🤠')
            back = types.KeyboardButton(f"🔙 Назад 🔙")
            markup.add(binfo, wtf, back)
            bot.send_message(message.chat.id, '🤠 Создатель 🤠', parse_mode='html', reply_markup=markup)
        elif message.text == '🤖 VK 🤖':
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("Посетить  VK создателя", url="https://vk.com/n1jel"))
            bot.send_message(message.chat.id, 'Перейдите на сайт', reply_markup=markup)
        elif message.text == '🤠 TG 🤠':
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("Посетить  TG создателя", url="https://t.me/N1jel"))
            bot.send_message(message.chat.id, 'Перейдите на сайт', reply_markup=markup)


        elif message.text == '🔙 Назад 🔙':
            mess = f'Привет <u><b>{message.from_user.first_name} {message.from_user.last_name} </b> </u>'
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            info = types.KeyboardButton(f'ℹ️ Информация ℹ️')
            website = types.KeyboardButton(f'🤠 Создатель 🤠')
            commands = types.KeyboardButton('👍🏿 Команды 👍🏿')
            rand = types.KeyboardButton(f"❓ Рандомное число ❓")
            markup.add(info, website, rand, commands)
            bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=markup)
        elif message.text == "Hello":
            bot.send_message(message.chat.id, "И тебе привет", parse_mode='html')
        elif message.text == "ID":
            bot.send_message(message.chat.id, f"Твой ID: {message.from_user.id}", parse_mode='html')
        elif message.text == "Photo":
            photo = open('icon.png', 'rb')
            bot.send_photo(message.chat.id, photo)
        else:
            bot.send_message(message.chat.id, "Я твоё не понимать, пиши осмысленные команды")

@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    a = ['Вау, говно, а не фото!', 'Классное фото, мне понравилось!', 'Ну даже не знаю, скорее всего говно']
    bot.send_message(message.chat.id, (random.choice(a)))

@bot.message_handler(content_types=['text'])
def get_user_text(message):
    else message.text == "Hello":
        bot.send_message(message.chat.id, "И тебе привет", parse_mode='html')
    elif message.text == "ID":
        bot.send_message(message.chat.id, f"Твой ID: {message.from_user.id}",  parse_mode='html')
    elif message.text == "Photo":
        photo = open('icon.png', 'rb')
        bot.send_photo(message.chat.id, photo)
    else:
        bot.send_message(message.chat.id, "Я твоё не понимать, пиши осмысленные команды")

bot.polling(none_stop=True)