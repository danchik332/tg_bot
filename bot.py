import telebot
from telebot import types
from config import token





userStep = {}

imageSelect = types.ReplyKeyboardMarkup(one_time_keyboard=True)  # create the image selection keyboard
imageSelect.add('Mickey', 'Minnie')

hideBoard = types.ReplyKeyboardRemove()  # if sent as reply_markup, will hide the keyboard


bot = telebot.TeleBot(token)

class Car:

    # Хэндлер для команды /car
    @bot.message_handler(commands=['car'])
    def send_car_info(message):
        # Получаем аргументы команды
        args = message.text.split()[1:]
        if len(args) != 2:
            bot.reply_to(message, "Неверный формат команды. Используйте: /car цвет марка")
            return
        # Получаем цвет и марку машины
        color, brand = args
        # Создаем экземпляр класса Car
        car = Car(color, brand)
        # Отправляем информацию о машине в чат
        bot.reply_to(message, car.info())

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)

# Handle '/start' and '/help'
@bot.message_handler(commands=['hello', 'start'])
def send_welcome(message):
    bot.send_message(message.chat.id, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")


@bot.message_handler(commands=['getImage'])
def command_image(m):
    cid = m.chat.id
    bot.send_message(cid, "Please choose your image now", reply_markup=imageSelect)  # show the keyboard
    userStep[cid] = 1

# Handle all other messages with content_type 'text' (content_types defaults to ['text'])




bot.infinity_polling()
