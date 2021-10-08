# coding: utf8
import json
import requests
import time
from urllib.parse import quote

google = 'http://google.com/complete/search?output=firefox&q='  # автодополенния на основе гугла
yandex = 'http://suggest.yandex.ru/suggest-ya.cgi?ct=text/html&v=2&part='  # автодополенния на основе яндекса

pharases = []  # пусто список для фраз


def fileTolist():
    file1 = open("phrase.txt", "r")
    while True:
        # считываем строку
        line = file1.readline()
        # прерываем цикл, если строка пустая
        if not line:
            break
        # добавляем в список фразы которые будем дополнять
        pharases.append(line.strip())
    # закрываем файл
    file1.close


def listToFile(l):
    # простая функция что построчно допысывает в файл каждый елемент списка.
    f = open('result.txt', 'w')
    for index in l:
        f.write(index + '\n')
    f.close()


fileTolist()  # считываем файл

allPharase = []
for phrase in pharases:
    print(phrase)
    r = requests.get(f'{google}+{phrase.replace(" ", "%20")}')  # сами запросы в гугл, + вписываю все в один список
    r = r.json()[1]
    for i in r:
        allPharase.append(i)

    r = requests.get(f'{yandex}+{quote(phrase)}') # сами запросы в яндекс, + вписываю все в один список
    help(r)
    r = r.text.replace('suggest.apply', '')[len(phrase)+4:-1]
    print(r)
    r = json.loads(r)

    r = r.text.replace('[', '').replace('"', '').replace(']', '').replace(')', '').split(',')  # исключеения всякой чипухи от яндекса
    del r[0:2]

    for i in r:
        allPharase.append(i)
    time.sleep(2)

listToFile(allPharase)  # создаем файл с созданными списками
