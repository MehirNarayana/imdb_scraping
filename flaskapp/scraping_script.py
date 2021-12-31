import re
import requests
from bs4 import BeautifulSoup
import random
import re


class Script:
    def __init__(self, number):
        self.data = requests.get('https://www.imdb.com/chart/top/')
        self.soup =  soup = BeautifulSoup(self.data.text, 'html.parser')
        self.all_movies = []
        self.number = number


    def find_element(self):
        for a in self.soup.find_all("td", class_="titleColumn"):
            self.all_movies.append(a.text)

    def get_movie(self):

        query = re.compile(r'\s*(\d+\.)\s+(.*)\s+(\(\d+\))')
        
        formatted_result = query.search(self.all_movies[self.number-1])
        number_result = formatted_result.group(1)
        name = formatted_result.group(2)
        date = formatted_result.group(3)
        print(number_result, name, date)
        return number_result, name, date
