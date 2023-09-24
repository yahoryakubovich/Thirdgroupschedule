import telebot
from telebot import types
from config import TOKEN

token = TOKEN
bot = telebot.TeleBot(token)

first_class = "Время: 13.40 - 15.00"
second_class = "Время: 15.10 - 16.30"
third_class = "Время: 16.40 - 18.00"
fourth_class = "Время: 18.20 - 19.40"

monday = [f"1. {first_class}, дисциплина: Теория перевода, преподаватель: Шаповалова А. Ф, кабинет: 811",
          f"2. {second_class}, дисциплина: ПУиПР, преподаватель: Давыдова C. А, кабинет: 715",
          f"3. {third_class}, дисциплина: Практическая грамматика, преподаватель: Кондратенко Т. Л, кабинет: 808",
          f"4. {fourth_class}, дисциплина: Основы американистики, преподаватель: Кондратенко Т. Л, кабинет: 811"
          ]

tuesday = [f"1. {first_class}, дисциплина: Просодия речи, преподаватель: Василина В. Н, кабинет: 716",
           f"2. {second_class}, дисциплина: Философия, преподаватель: Екадумов А. И, кабинет: 811",
           f"3. {third_class}, дисциплина: Философия, преподаватель: Екадумов А. И, кабинет: 811",
           ]

wednesday = [f"1. {first_class}, дисциплина: Практическая фонетика 2, преподаватель: Супринович О. Е, кабинет: 711",
             f"2. {second_class}, дисциплина: Просодия речи, преподаватель: Василина В. Н, кабинет: 716",
             f"3. {third_class}, дисциплина: Практическая фонетика 2, преподаватель: Супринович О. Е, кабинет: 713",
             ]

thursday = [f"1. {second_class}, дисциплина: Практическая грамматика 2, преподаватель: Лобанова Т. С, кабинет: 713",
            f"2. {third_class}, дисциплина: ПУиПР, преподаватель: Давыдова C. А, кабинет: 716",
            ]

friday = [
    f"1. {first_class}, дисциплина: Диалектология и лингвогеография иностранного языка, преподаватель: Никитенко Т. В, кабинет: 811",
    f"2. {second_class}, дисциплина: Социология, преподаватель: Безнюк Д. К, кабинет: 811",
    f"3. {third_class}, дисциплина: Практическая грамматика, преподаватель: Кондратенко Т. Л, кабинет: 715",
    f"4. {fourth_class}, дисциплина: Аналитическое чтение, преподаватель: Цвирко Е. И, кабинет: 716"
]

saturday = ["Пары отсутствуют"]

# Создаем клавиатуру для кнопки "Узнать расписание"
markup_start = types.ReplyKeyboardMarkup(resize_keyboard=True)
item_start = types.KeyboardButton("Узнать расписание")
markup_start.add(item_start)

# Создаем клавиатуру для кнопок дней недели
markup_days = types.ReplyKeyboardMarkup(resize_keyboard=True)
item_monday = types.KeyboardButton("Понедельник")
item_tuesday = types.KeyboardButton("Вторник")
item_wednesday = types.KeyboardButton("Среда")
item_thursday = types.KeyboardButton("Четверг")
item_friday = types.KeyboardButton("Пятница")
item_saturday = types.KeyboardButton("Суббота")
markup_days.add(item_monday, item_tuesday, item_wednesday, item_thursday, item_friday, item_saturday)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, напиши день, чтобы узнать его расписание!', reply_markup=markup_start)


@bot.message_handler(content_types=['text'])
def message_reply(message):
    if message.text == "Узнать расписание":
        bot.send_message(message.chat.id, 'Выбери день недели:', reply_markup=markup_days)
    elif message.text == "Понедельник":
        for x in monday:
            bot.send_message(message.chat.id, f"{x}")
    elif message.text == "Вторник":
        for x in tuesday:
            bot.send_message(message.chat.id, f"{x}")
    elif message.text == "Среда":
        for x in wednesday:
            bot.send_message(message.chat.id, f"{x}")
    elif message.text == "Четверг":
        for x in thursday:
            bot.send_message(message.chat.id, f"{x}")
    elif message.text == "Пятница":
        for x in friday:
            bot.send_message(message.chat.id, f"{x}")
    elif message.text == "Суббота":
        for x in saturday:
            bot.send_message(message.chat.id, f"{x}")


bot.infinity_polling()
