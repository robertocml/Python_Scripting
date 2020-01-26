from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome2
import pandas as pd
import time

path = 'C:\\Users\\rober\Downloads\\archives\\chromedriver_win32\\chromedriver.exe'
chrome_options = Options()
chrome_options.add_argument("- incognito")
browser = webdriver.Chrome(path, options=chrome_options)
pages = 3
url = 'http://books.toscrape.com/catalogue/page-1.html'


def getdata(start_url, pgs):
    current = 0
    urls = browser.get(start_url)


print("Testing pycharm vcs.")
