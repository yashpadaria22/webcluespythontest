import requests
from bs4 import BeautifulSoup
url=["https://en.wikipedia.org/wiki/Python_(programming_language)"]
for i in range(len(url)):
    responce=requests.get(url[i])
    soup=BeautifulSoup(responce.text,'html.parser')
    contant=soup.prettify()
    file_name="scrap"+str(i)+".txt"
    with open(file_name, 'w',encoding='utf-8') as file:
        file.write(contant)