from bs4 import BeautifulSoup
from urllib.request import urlopen
import wikipedia

wikipedia.set_lang('ru')


def weather():
    html = urlopen('https://yandex.ru/pogoda/krasnoyarsk').read().decode('utf8')
    soup = BeautifulSoup(html, 'html.parser')

    wthr = soup.find_all('div', attrs={'class': 'temp fact__temp fact__temp_size_s'})
    wthr = wthr[0]

    weather = wthr.find(class_='temp__value').get_text()

    text = f'In Krasnoyarsk now: {weather}°С'

    return text

print(weather())

def search_wiki(access):
    result = wikipedia.summary(access, sentences=5)
    return result
