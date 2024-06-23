# pip install webdriver_manager

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

import pandas as pd

import time

# 크롬 실행시에 필요한 옵션들 초기화
chrome_options = Options()
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--window-size=1920,1000")

# 크롬드라이버 초기화
service = Service(executable_path="./chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)

# 웹 페이지 열기
base_url = 'http://www.cine21.com'
ranking_url = base_url + '/rank/boxoffice/domestic'
driver.get(ranking_url)

# 페이지 소스 가져오기...
page_source = driver.page_source

# BS4로 전달해서 파싱하기
soup = BeautifulSoup(page_source, 'html.parser')

# 영화 목록을 담기 위한 빈 변수
data = []

boxoffice_list_content = soup.find('div', id='boxoffice_list_content')
# print(boxoffice_list_content)
# 영화 순위, 영화 제목과, 관객수 출력하시오.
boxoffice_li_list = boxoffice_list_content.find_all('li', class_='boxoffice_li')
for boxoffice_li in boxoffice_li_list:
    mov_name_div = boxoffice_li.find('div', class_='mov_name')
    people_num_div = boxoffice_li.find('div', class_='people_num')
    rank_num_span = boxoffice_li.find('span', class_='grade')

    mov_link = base_url + boxoffice_li.find('a')['href']

    rank = rank_num_span.get_text(strip=True)
    mov_name = mov_name_div.get_text(strip=True)
    people_num = people_num_div.get_text(strip=True).replace('관객수|', '')
    
    # print(f"순위: {rank}, 영화 제목: {mov_name}, 관객수: {people_num}")
    data.append({'순위': rank, '영화제목': mov_name, '관객수': people_num, '웹사이트정보': mov_link})
    
# 잠시 기다리기 5초간 대기...
# time.sleep(5)
# print(data)
    
df = pd.DataFrame(data)
# # 엑셀로 저장
df.to_excel('boxoffice_rankings.xlsx')

time.sleep(5)

# 브라우저 닫기
driver.quit()
