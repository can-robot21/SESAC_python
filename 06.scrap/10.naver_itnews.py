import requests
from bs4 import BeautifulSoup

url = "https://news.naver.com/section/105"

data = requests.get(url)
soup = BeautifulSoup(data.text, 'html.parser')

# 신문 기사제목 및 링크 출력하기
# 헤드라인 섹션 가져오기

section_articles = soup.select('div.section_latest > div > div.section_latest_article._CONTENT_LIST._PERSIST_META')

for section_article in section_articles:
    sa_text_titles = section_article.find_all('a', class_='sa_text_title')
    for sa_text_title in sa_text_titles:
        print(sa_text_title.get_text().strip())

print('-' * 50)

section_articles = soup.select('div.section_article._TEMPLATE')

for section_article in section_articles:
    sa_text_titles = section_article.find_all('a', class_='sa_text_title')
    for sa_text_title in sa_text_titles:
        print(sa_text_title.get_text().strip())
