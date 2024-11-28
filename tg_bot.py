import random
import telebot

def get_random_anwser():
    answers = ["Нормально", "Супер", "Класс"]
    return random.choice(answers)

def run(token):
    bot = telebot.TeleBot(token, parse_mode=None)

    @bot.message_handler(commands=['start', 'help'])
    def send_welcome(message):
        bot.reply_to(message, "Привет! Я бот и я могу рассказать как у меня дела")

    @bot.message_handler(func=lambda message: True)
    def echo_all(message):
        if message.text == "Как дела?":
            answer = get_random_anwser();
            bot.send_message(message.chat.id, answer)
        else:
            bot.send_message(message.chat.id, "Я могу только ответить на вопрос: Как дела?")

    bot.infinity_polling()