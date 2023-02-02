import requests
from bs4 import BeautifulSoup as BS

from module.base import get_cars


def pars():
    """
    Функция для парсинга первых пяти страниц
    """
    for p in range(1,6):
        URL = f'https://www.mashina.kg/search/all/?page={p}'
        response = requests.get(URL)
        if response.status_code == 200:
            soup = BS(response.text, 'html.parser')
            ads_table = soup.find('div', class_='table-view-list')
            ad_cards = ads_table.find_all('div', class_='list-item')
            cars = []
            for c in ad_cards:
                title = c.find('h2', class_='name').string.replace('\n', '').strip()
                price = c.find('div', class_='price').find('strong').string.replace('\n', '').strip()
                info = c.find(
                    'div', class_='block info-wrapper item-info-wrapper'
                              ).find('p', class_='body-type').string.replace('\n', '').strip()
                link = 'https://www.mashina.kg'+c.a['href']
                cars.append((title, price, info, link))
            get_cars(cars)