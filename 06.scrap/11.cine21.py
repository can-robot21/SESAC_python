import requests
from bs4 import BeautifulSoup

url = 'http://www.cine21.com/rank/boxoffice/domestic'
response = requests.get(url)

# 응답 텍스트를 BeautifulSoup 로 파싱
soup = BeautifulSoup(response.text, 'html.parser')
# print(soup)

boxoffice_list_content = soup.select_one('boxoffice_')