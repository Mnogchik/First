from bs4 import BeautifulSoup  # импортируем библиотеку BeautifulSoup
import requests  # импортируем библиотеку requests


def parse1():
    url1 = 'https://www.imdb.com/chart/top/?ref_=nv_td_mv250'  # передаем необходимы URL адрес
    page1 = requests.get(url1)  # отправляем запрос методом Get на данный адрес и получаем ответ в переменную
    print(page1.status_code)  # смотрим ответ
    dictionary = {}
    soup1 = BeautifulSoup(page1.text, "html.parser")  # передаем страницу в bs4

    block1 = soup1.findAll('tr')  # находим контейнер с нужным классом
    for data in block1:  # проходим циклом по содержимому контейнера
        title = ''
        rating = ''

        temp1 = data.find('td', class_='titleColumn')
        if temp1 is not None:
            title = temp1.text.split()

        temp2 = data.find('td', class_='ratingColumn imdbRating')
        if temp2 is not None:
            rating = temp2.text.split()

        if title != '' and rating != '':
            dictionary[str(title)] = str(rating)
    return dictionary


if __name__ == '__main__':
    print(parse1())
