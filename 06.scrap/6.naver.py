import requests
from bs4 import BeautifulSoup

url = "https://sports.news.naver.com/index"

data = requests.get(url)
soup = BeautifulSoup(data.text, 'html.parser') # 기본 파서 html.parser 와 추가로 lxml 설치해 사용 가능한 더 좋은 파서가 있음.
print(soup)

# 신문 기사제목 및 링크 출력하기

news_list = soup.select_one(".today_list li")
# print(len(today_list))

for news in news_list:
    div_tag = news.select_one('.title')
    print(div_tag.text)