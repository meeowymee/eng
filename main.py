# -*- coding: utf8 -*-
import telebot
from telebot import types
bot = telebot.TeleBot('YOUR_TOKEN')
 
@bot.message_handler(commands=['start'])
def start(message):
    mess = f"Привіт, мене звуть Рікі!🦆 Мене було створено для того щоб навчити людей простим часам англійської мови. Я можу дати коротке пояснення та відправити посилання на дуже корисні сайти! "
    bot.send_message(message.chat.id, mess, parse_mode='html')
 
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    simple = types.KeyboardButton('Past Simple')
    present = types.KeyboardButton('Present Simple')
    future = types.KeyboardButton('Future Simple')
 
    markup.add(simple,present,future)
    bot.send_message(message.chat.id, ' Що будемо вчити? ' , reply_markup=markup)
@bot.message_handler()
def get_user_text(message):
    if message.text == "Past Simple":
        bot.send_message(message.chat.id, 'Past Simple - це простий минулий час,який використовується коли ми кажемо про завершену дію в минулому. Використовувати його неймовірно easy. ')
        bot.send_message(message.chat.id, 'Головна складність: Past Simple утворюється за допомогою перетворення дієслова у форму минулого часу. Якщо дію виражено правильним дієсловом,то до його першої форми додається закінчення -ed. Якщо використовується неправильне дієслово,застосовується друга форма неправильного дієслова з таблиці неправильних дієслів. Якщо потрібного дієслова там немає - значить,воно правильне і до нього можна додавати закінчення -ed.')
        bot.send_message(message.chat.id, 'Таблиця неправильних дієслів: https://pin.it/2mrgcJI')
        bot.send_message(message.chat.id, 'Більше інформації: https://grammarway.com/ua/past-simple')
        bot.send_message(message.chat.id, 'Тренажер: https://onlinetestpad.com/ua/test/461287-past-simple')
    elif message.text == 'Present Simple':
        bot.send_message(message.chat.id, 'Present Simple - це простий теперішній час. Використовуючи цей час, люди розповідають про свої звички та інші регулярні дії, також про наукові факти та речі, які завжди правдиві. Наприклад, хобі, розпорядок дня чи події.')
        bot.send_message(message.chat.id, 'Більше інформації: https://grammarway.com/ua/present-simple')
        bot.send_message(message.chat.id, 'Тренажер: https://onlinetestpad.com/ru/test/10222-present-simple')
    elif message.text == 'Future Simple':
        bot.send_message(message.chat.id, 'Future Simple - е простий майбутній час. Його використовують, коли йдеться про спонтанні рішення, події в майбутньому, на які ми не можемо вплинути, обіцянки, попередження і навіть погрози.')
        bot.send_message(message.chat.id, 'Більше інформації: https://grammarway.com/ua/future-simple')
        bot.send_message(message.chat.id, 'Тренажер: https://onlinetestpad.com/ru/test/1498997-future-simple')
    elif message.text == 'Hi':
        bot.send_message(message.chat.id, 'sup')
    else:
        bot.send_message(message.chat.id, 'huh??')
 
bot.polling(none_stop=True)