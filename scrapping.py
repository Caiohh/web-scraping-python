from bs4 import BeautifulSoup
import requests

# Site que será coletado
site = "http://www.pudim.com.br/"

# Coleta de dados do site
html = requests.get(site).content
dados = BeautifulSoup(html, 'html.parser')
email = dados.find("div", class_="email")

# coletando a tag dentro da div email
link = email.find("a")
print("1", link)  
print("2", link.text)
print("3", link.attrs['href'])
