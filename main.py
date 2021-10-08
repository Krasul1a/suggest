# coding: utf8

import json
import requests
import time
from urllib.parse import quote
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
}
searchDict = {'google': 'http://google.com/complete/search?output=firefox&q=',
              'yandex': 'http://suggest.yandex.ru/suggest-ya.cgi?ct=text/html&v=2&part=',
              'bing': 'https://api.bing.com/osjson.aspx?query=',
              'duckduckgo': 'https://duckduckgo.com/ac/?kl=wt-wt&q=',
              'qwant': 'https://api.qwant.com/api/suggest/?client=opensearch&q=',
              'yahoo': 'https://api.search.yahoo.com/sugg/gossip/gossip-in-ura?output=sd1&command=',
              'startpage': 'https://www.startpage.com/suggestions?q=',
              'dogpile': 'https://www.dogpile.com/suggestions?q=',
              'swisscows': 'https://swisscows.com/api/suggest?query=',
              'ask': 'https://amg-ss.ask.com/query?q=',
              'brave': 'https://search.brave.com/api/suggest?q='}

pharases = []  # пусто список для фраз

def fileTolist():
    file1 = open("phrase.txt", "r")
    while True:
        # считываем строку
        line = file1.readline()
        # прерываем цикл, если строка пустая
        if not line:
            break
        # добавляем в список фразы которые будем дополнять и сразу переводим в URL форму
        pharases.append(line.strip().replace(' ', '%20'))
    # закрываем файл
    file1.close

def listToFile(l):
    # простая функция что построчно допысывает в файл каждый елемент списка.
    f = open('result.txt', 'w')
    for index in l:
        f.write(index + '\n')
    f.close()



def suggestGoogle(phrase):
    r = requests.get(f"{searchDict['google']}{phrase.replace(' ', '%20')}")
    r = r.json()[1]
    return r


def suggestYandex(phrase):
    r = requests.get(f"{searchDict['yandex']}{quote(phrase)}")
    r = r.text.replace('suggest.apply', '')[len(phrase) + 4:-1]
    r = json.loads(r)
    return r

def suggestBing(phrase):
    r = requests.get(f"{searchDict['bing']}{quote(phrase)}")
    r = r.json()[1]
    return r

def suggestDuckduckgo(phrase):
    r = requests.get(f"{searchDict['duckduckgo']}{quote(phrase)}")
    r = r.json()
    phrases = []
    for i in r:
        phrases.append(i['phrase'])
    return phrases

def suggestQwant(phrase):
    r = requests.get(f"{searchDict['qwant']}{quote(phrase)}")
    r = r.json()[1]
    return r

def suggestYahoo(phrase):
    r = requests.get(f"{searchDict['yahoo']}{quote(phrase)}")
    r = r.json()['r']
    phrases = []
    for i in r:
        phrases.append(i['k'])
    return phrases

def suggestStartpage(phrase):
    r = requests.get(f"{searchDict['startpage']}{quote(phrase)}")
    r = r.json()['suggestions']
    phrases = []
    for i in r:
        phrases.append(i['text'])
    return phrases

def suggestDogpile(phrase):  # пока не работает просит капчу
    r = requests.get(f"{searchDict['dogpile']}{quote(phrase)}",headers=headers)
    return r

def suggestSwisscows(phrase):
    r = requests.get(f"{searchDict['swisscows']}{quote(phrase)}")
    r = r.json()
    return r


def suggestAsk(phrase):
    r = requests.get(f"{searchDict['ask']}{quote(phrase)}")
    r = r.json()[1]
    return r

def suggestBrave(phrase): 
    r = requests.get(f"{searchDict['brave']}{quote(phrase)}&source=web",headers=headers)
    r = r.json()[1]
    return r
