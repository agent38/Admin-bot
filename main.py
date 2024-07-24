import telebot
from dotenv import load_dotenv
import os

load_dotenv()

OurChatId = -1002070474085
MyID = 1006283458

bot = telebot.TeleBot(os.getenv("Token"))

@bot.message_handler(commands = [("start")])
def Start(message):
    bot.send_message(message.chat.id, "ok")

@bot.message_handler(commands = [("fuck_you")])
def FuckYou(message):
    bot.send_message(OurChatId, "ДА ПОШЛИ ВЫ ВСЕ НАХУЙ Я МИКРОВОЛНОВКА ГОВОРЯЩАЯ")

@bot.message_handler(func = lambda  message: True)
def CheckMat(message):
    with open('StopWord.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()

    lines = [line.strip() for line in lines]

    for i in lines:
        if i in message.text.lower():
            bot.reply_to(message, f"Сам {message.text}. Хуесос ебаный")


bot.polling(none_stop = 0.15)