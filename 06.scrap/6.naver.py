import requests
from bs4 import BeautifulSoup

url = "https://sports.news.naver.com/index"

data = requests.get(url)
soup = BeautifulSoup(data.text, 'html.parser')
print(soup)

# 신문 기사제목 및 링크 출력하기

news_list = soup.select_one(".today_list li")
# print(len(today_list))

for news in news_list:
    a_tag = news.select_one('a')
    print(a_tag['title'])
    print(a_tag['href'])