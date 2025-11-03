from bs4 import BeautifulSoup
import requests
url="https://github.com/SanjaySivakumar2005"
page=requests.get(url)
soup=BeautifulSoup(page.text,'html.parser')
print(soup)
file=open("scrap.txt",'w+',encoding='utf-8')
file.write(soup.get_text())