import telebot
import requests
from telebot import types

global city
global cityy


weather_token = "f226910c0ac7a1841df49a9c1c7d0e4c"
bot = telebot.TeleBot('5123025838:AAFEW5qcrLje8AyNMOQcaxEgAS4tRIpJ-Xo')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет, я бот, используйте команду:\n/now - нынешняя погода\n/five - погода на "
                                      "5 дней ")

@bot.message_handler(commands=['now'])
def startf(message):
    global t, s
    t = 'three'
    s = ''
    bot.send_message(message.chat.id, "Введите город")



@bot.message_handler(commands=['five'])
def start(message):
    global s, t
    s = 'seven'
    t = ''
    bot.send_message(message.chat.id, "Введите город(погода на 5 дней)")



@bot.message_handler(content_types='text')
def answer(message):
    global s
    global t
    if s == 'seven':
        try:
            city = message.text.lower()
            res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                               params={'q': city, 'units': 'metric', 'cnt': 40, 'lang': 'ru',
                                       'APPID': weather_token})
            data = res.json()

            #    bot.send_message(message.chat.id, data)
            bot.send_message(message.chat.id, "Прогноз погоды на 5 дней:")
            for i in range(0, len(data['list']), 8):
                bot.send_message(message.chat.id, f"Дата: < {data['list'][i]['dt_txt']} >"
                                                  f"\nТемпература: <{'{0:+3.0f}'.format(data['list'][i]['main']['temp'])} °C > "
                                                  f"\nПогодные условия: <{data['list'][i]['weather'][0]['description']}>"
                                                  f"\nСкорость ветра:<{data['list'][i]['wind']['speed']} м/c>")
                #bot.send_message(message.chat.id, f"if z == 7, {s}")
            s = ''

        except Exception:
            bot.send_message(message.chat.id, "Проверьте название города")

        t = ''
        s = ''

    if t == 'three':
        try:
            cityy = message.text.lower()
            res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                               params={'q': cityy, 'units': 'Metric', 'lang': 'ru', 'cnt': 5, 'APPID': weather_token})
            data = res.json()
            #bot.send_message(message.chat.id, f"if z == 3, {t}")
            bot.send_message(message.chat.id, f"Город: {cityy}"
                                              f"\nПогодные условия:{data['weather'][0]['description']}"
                                              f"\nТемпература: {data['main']['temp']}°C"
                                              f"\nМинимальная температура: {data['main']['temp_min']}°C"
                                              f"\nМаксимальная температура {data['main']['temp_max']}°C")
        except Exception:
            bot.send_message(message.chat.id, "Проверьте название города")



bot.polling()
