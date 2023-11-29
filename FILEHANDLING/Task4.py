import requests
from bs4 import BeautifulSoup
url="https://en.wikipedia.org/wiki/Python_(programming_language)"
responce=requests.get(url)
soup=BeautifulSoup(responce.text,'html.parser')
contant=soup.prettify()
with open('scrap.txt', 'w',encoding='utf-8') as file:
    file.write(contant)