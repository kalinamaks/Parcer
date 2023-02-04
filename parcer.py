import requests
from bs4 import BeautifulSoup

# Ввод URL и получение код ответа
url = input("Введите URL: ")
response = requests.get(url)
print(response)

# Получаем контент страницы
page = requests.get(url)

# Парсим страницу
soup = BeautifulSoup(page.content, 'html.parser')

# Получаем метаданные
meta_tags = soup.find_all('meta')

# Выводим метаданные
for item in meta_tags:
    print(item.attrs)