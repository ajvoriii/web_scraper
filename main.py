import requests
from bs4 import BeautifulSoup as bs

url = 'https://www.google.com/search?q=python+programming'
r = requests.get(url)
soup = bs(r.text, 'html.parser')

for i in soup.find_all('a'):
    print(i.get('href'))
