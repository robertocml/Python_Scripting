# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver import Chrome2
# import pandas as pd
# import time
import requests
import pandas as pd
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

df = pd.DataFrame(columns=["Title","Price","Rating","Stock"])

articles = soup.find_all('article')


for each in articles:
    rating = each.findChild("p")['class'][1]
    title = each.findChild("h3").findChild("a")['title']
    price = each.find_all("div")[1].findChild("p").text
    stock = each.find_all("div")[1].select('div > p')[1].get_text(strip=True)

    row = [title, price, rating, stock]
    df.loc[len(df)] = row

df.to_csv("Books_Scraped.csv", index=False)
print(df)
