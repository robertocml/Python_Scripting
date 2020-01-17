import requests
from bs4 import BeautifulSoup
 
req = requests.get('https://news.google.com/?hl=es-419&gl=MX&ceid=MX:es-419')
soup = BeautifulSoup(req.text, "lxml")

for tag in soup.find_all('a'):
    print (tag.text)

