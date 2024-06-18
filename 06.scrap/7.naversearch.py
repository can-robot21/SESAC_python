import requests
from bs4 import BeautifulSoup

base_url = "https://search.naver.com/search.naver"

def naver_search(query):
    params = {"query": query}
    
    response =requests.get(base_url, params=params)
    return response.text

word = '파이썬 프로그래밍'
soup = naver_search(word)

print(soup)
