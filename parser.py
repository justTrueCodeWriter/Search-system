import requests
from bs4 import BeautifulSoup

url = 'https://www.kinopoisk.ru'

headers = {
    "Accept": '*/*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.133 Safari/537.36'
}

src = requests.get(url=url, headers=headers).text
