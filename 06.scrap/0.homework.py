import requests
from bs4 import BeautifulSoup

url = "https://news.naver.com/section/105"

data = requests.get(url).text

soup = BeautifulSoup(data, 'html.parser')
news = soup.select_one('ul#_SECTION_HEADLINE_LIST_6rmsc')