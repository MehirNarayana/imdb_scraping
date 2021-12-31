import re
import requests
from bs4 import BeautifulSoup
import random


data = requests.get('https://www.imdb.com/chart/top/')


soup = BeautifulSoup(data.text, 'html.parser')



all_movies = []

for a in soup.find_all("td", class_="titleColumn"):
    all_movies.append(a.text)
