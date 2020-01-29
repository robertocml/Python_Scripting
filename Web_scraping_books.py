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

test = soup.find_all('h3')

# Getting the titles
for each_a in test:
    for each_title in each_a:
        print(each_title['title'])