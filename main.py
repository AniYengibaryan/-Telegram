
import requests 
import time
import telebot
import os
import copy


bot = telebot.TeleBot('<token>')
CHANNEL_NAME = 'name'
# f = open('data.csv', 'r', encoding='UTF-8')

with open('rub/data.csv', 'rb') as f:
    try:  # catch OSError in case of a one line file 
        f.seek(-2, os.SEEK_END)
        while f.read(1) != b'\n':
            f.seek(-2, os.SEEK_CUR)
    except OSError:
        f.seek(0)
    last_line = f.readline().decode()



with open('dollar/data_dollar.csv', 'rb') as f:
    try:  # catch OSError in case of a one line file 
        f.seek(-2, os.SEEK_END)
        while f.read(1) != b'\n':
            f.seek(-2, os.SEEK_CUR)
    except OSError:
        f.seek(0)
    last_line2 = f.readline().decode()



with open('eur/data_eur.csv', 'rb') as f:
    try:  # catch OSError in case of a one line file 
        f.seek(-2, os.SEEK_END)
        while f.read(1) != b'\n':
            f.seek(-2, os.SEEK_CUR)
    except OSError:
        f.seek(0)
    last_line3 = f.readline().decode()


a=1
# img = open('currey.jpeg','rb')
while a < 10:
    bot.send_message(CHANNEL_NAME,"Курс рубль-драм",last_line)
    bot.send_message(CHANNEL_NAME,"Курс доллар-драм",last_line2)
    bot.send_message(CHANNEL_NAME,"Курс евро-драм",last_line3)
     # Делаем паузу в один час
    # time.sleep()
    bot.send_photo(CHANNEL_NAME,open('rub/currey.jpeg','rb'))
    bot.send_photo(CHANNEL_NAME,open('dollar/currey_dollar.jpeg','rb'))
    bot.send_photo(CHANNEL_NAME,open('eur/currey_eur.jpeg','rb'))
    time.sleep(3)

# print(last_line)


bot.polling(none_stop=True, interval=0)
