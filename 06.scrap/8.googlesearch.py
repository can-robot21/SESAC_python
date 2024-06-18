import requests
from bs4 import BeautifulSoup

base_url = "https://www.google.com/search"

def google_search(query):
    params = {"q": query}
    
    response =requests.get(base_url, params=params)
    return response.text

word = '파이썬 프로그래밍'
soup = google_search(word)

print(soup)
