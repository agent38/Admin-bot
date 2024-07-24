import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
import telebot
import time

load_dotenv()

bot = telebot.TeleBot(os.getenv("Token"))

OurChatId = -1002070474085
MyID = 1006283458

Citis = ["Донецк", "Макеевка", "Харцизк", "Торез", "Авдеевка", "Пески", "Ясиноватая", "Бахмут", "Таганрог", "Ростов"]

OtherCitis = ["Гурзуф", "Ялта", "Алушта"]


def GetWeather():
    try:
        for i in Citis:
            url = f"https://www.google.com/search?q=погода+{i}+на+завтра"
            IsNone = False
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
            }
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')

                WeatherCondition = soup.find('div', class_='BNeawe tAd8D AP7Wnd').text

                if WeatherCondition != None:
                    IsNone = False
                elif WeatherCondition == None:
                    IsNone = True


                with open("Weather.txt", "w") as file:
                    file.write(WeatherCondition)

                if IsNone == False:
                    print(i)
                    break
                elif IsNone == True:
                    pass

    except Exception as e:
        print(e)

def GetWeatherInOtherCiti(): #она нужна если кто то уехал в другой город
    try:
        for i in OtherCitis:
            url = f"https://www.google.com/search?q=погода+{i}+на+завтра"
            IsNone = False
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
            }
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')

                WeatherCondition = soup.find('div', class_='BNeawe tAd8D AP7Wnd').text

                if WeatherCondition != None:
                    IsNone = False
                elif WeatherCondition == None:
                    IsNone = True


                with open("WeatherInOtherCiti.txt", "w") as file:
                    file.write(WeatherCondition)


                if IsNone == False:
                    print(i)
                    break
                elif IsNone == True:
                    pass

    except Exception as e:
        print(e)
def RemoveLines(filename, lines_to_remove):
    with open(filename, 'r') as file:
        lines = file.readlines()

    with open(filename, 'w') as file:
        for number, line in enumerate(lines):
            if number not in lines_to_remove:
                file.write(line)


# Удалить 2-ю и 4-ю строки (нумерация начинается с 0)
# remove_lines('weather.txt', [1, 3])

def RemoveCharacters(filename, chars_to_remove):
    with open(filename, 'r') as file:
        content = file.read()

    for char in chars_to_remove:
        content = content.replace(char, '')

    with open(filename, 'w') as file:
        file.write(content)


# Удалить символы 'a' и 'b'
# remove_characters('weather.txt', ['a', 'b'])

def RemoveWords(filename, words_to_remove):
    with open(filename, 'r') as file:
        content = file.read()

    for word in words_to_remove:
        content = content.replace(word, '')

    with open(filename, 'w') as file:
        file.write(content)


# Удалить слова 'weather' и 'forecast'
# remove_words('weather.txt', ['weather', 'forecast'])


def ReadSpecificLine(filename, line_number):
    with open(filename, 'r') as file:
        lines = file.readlines()
        if line_number < len(lines):
            return lines[line_number].strip()  # .strip() удаляет лишние пробелы и символы новой строки
        else:
            return None
            # Возвращает None, если строка с таким номером отсутствует


GetWeather()

RemoveLines("Weather.txt", [0])
RemoveCharacters("Weather.txt", ['°', 'F'])
RemoveWords("Weather.txt", ["Partly", "High: ", "Low: "])
Weather = ReadSpecificLine("Weather.txt", 0)
x = ReadSpecificLine("Weather.txt", 1)

MaxTemperature = x[:-3]
MinTemperature = x[3:]
Weather.strip()

del x

MaxTemperature = (int(MaxTemperature) - 32) * 5 / 9
MinTemperature = (int(MinTemperature) - 32) * 5 / 9

GetWeatherInOtherCiti()

RemoveLines("WeatherInOtherCiti.txt", [0])
RemoveCharacters("WeatherInOtherCiti.txt", ['°', 'F'])
RemoveWords("WeatherInOtherCiti.txt", ["Partly", "High: ", "Low: "])
WeatherInOtherCiti = ReadSpecificLine("WeatherInOtherCiti.txt", 0)
y = ReadSpecificLine("WeatherInOtherCiti.txt", 1)

MaxTemperatureInOtherCiti = y[:-3]
MinTemperatureInOtherCiti = y[3:]
WeatherInOtherCiti.strip()

del y

MaxTemperatureInOtherCiti = (int(MaxTemperatureInOtherCiti) - 32) * 5 / 9
MinTemperatureInOtherCiti = (int(MinTemperatureInOtherCiti) - 32) * 5 / 9

bot.send_message(OurChatId, f"В Донецке\nПогода {Weather} \nМаксимальная температура {int(MaxTemperature)} \nМинимальная температура {int(MinTemperature)}")
bot.send_message(OurChatId, f"В артеке\nПогода {WeatherInOtherCiti}\nМаксимальная температура {int(MaxTemperatureInOtherCiti)}\nМинимальная температура {int(MinTemperatureInOtherCiti)}")

time.sleep(1)
if(MaxTemperature > MaxTemperatureInOtherCiti):
    x = MaxTemperature - MaxTemperatureInOtherCiti
    if x <= 3:
        bot.send_message(OurChatId, "Нам пизда")
    else:
        bot.send_message(OurChatId, "Не жалуйтесь")
        time.sleep(1)
        bot.send_message(OurChatId, "Нам тут пизда")

elif(MaxTemperatureInOtherCiti > MaxTemperature):
    x = MaxTemperatureInOtherCiti - MaxTemperature
    if x <= 3:
        bot.send_message(OurChatId, "Нам пизда")
    else:
        bot.send_message(OurChatId, "Press F")
        time.sleep(1)
        bot.send_message(OurChatId, "Вам пизда")