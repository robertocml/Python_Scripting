# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver import Chrome2
# import pandas as pd
# import time
import requests
from bs4 import BeautifulSoup

# Version with Selenium......
# path = 'C:\\Users\\rober\Downloads\\archives\\chromedriver_win32\\chromedriver.exe'
# chrome_options = Options()
# chrome_options.add_argument("- incognito")
# browser = webdriver.Chrome(path, options=chrome_options)
# pages = 3

req = requests.get('http://books.toscrape.com/catalogue/page-1.html')
soup = BeautifulSoup(req.text, "lxml")

url = 'http://books.toscrape.com/catalogue/page-1.html'

for tag in soup.find_all('a'):
    print(tag.text)


body = soup.find("article", {'class':'product_prod'}).get_text()
print(len(body))
