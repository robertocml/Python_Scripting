# Basic Scraping using bs4
import requests
import pandas as pd
from bs4 import BeautifulSoup

# list for storing all reqs
reqs = []

#Getting the reqs from test web
for x in range(1, 51):
    reqs.append(requests.get('http://books.toscrape.com/catalogue/page-' + str(x) + '.html'))

# Creating the df
df = pd.DataFrame(columns=["Title", "Price", "Rating", "Stock"])

# Scraping all info from all 50 pages in the website...
for x in range(0, 50):
    soup = BeautifulSoup(reqs[x].text, "lxml")
    articles = soup.find_all('article')
    for each in articles:
        rating = each.findChild("p")['class'][1]
        title = each.findChild("h3").findChild("a")['title']
        price = each.find_all("div")[1].findChild("p").text
        stock = each.find_all("div")[1].select('div > p')[1].get_text(strip=True)
        row = [title, price, rating, stock]
        df.loc[len(df)] = row
        df['Price'] = df['Price'].str[-5:]

# Creating a csv with info..
df.to_csv("Books_Scraped.csv", index=False)
