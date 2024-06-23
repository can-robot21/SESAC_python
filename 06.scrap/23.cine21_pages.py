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

# DB 초기화
conn, cur = my_db.init_db()

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

def get_movie_list():
    boxoffice_list_content = soup.fine('div', id = 'boxoffice_list_content')
    # print(boxoffice_list_content)
    # 영화 순위, 영화 제목과, 관객수 출력하시오.
    boxoffice_li_list = boxoffice_list_content.find_all('li', class_='boxoffice_li')
    for boxoffice_li in boxoffice_li_list:
        mov_name_div = boxoffice_li.find('div', class_='mov_name')
        people_num_div = boxoffice_li.find('div', class_='people_num')
        rank_num_span = boxoffice_li.find('span', class_='grade')

        # mov_link = base_url + boxoffice_li.find('a')['href']
        a_link = boxoffice_li.find_element(Bu.TAG_NAME, 'a')

        rank = rank_num_span.text.strip()
        mov_name = mov_name_div.text.strip()
        people_num = people_num_div.text.strip().replace('관객수|', '')
        
        # print(f"순위: {rank}, 영화 제목: {mov_name}, 관객수: {people_num}")
        data.append({'순위': rank, '영화제목': mov_name, '관객수': people_num, '웹사이트정보': mov_link})
        
        my_db.save_to_db(conn, cur, rank, mov_name, people_num, mov_link)
        

# 첫 페이지 부르기
get_movie_list()

# 잠시 기다리기 5초간 대기...
# time.sleep(5)
    
# 두번째 페이지 가져오기
for page in range(2, 10):
    print(f'현재 {page}를 분석 중입니다.')
    
    # 페이지 목록 div 가 뜰때까지 기다린다.
    # page_tags = driver.find_elements(By.CSS_SELECTOR, 'div.page a')
    
    page_tags = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.page a')))
    page_tags[page]click()
    
    # time.sleep(5)
    # 혹시 모르니.. 클릭 한 이후에 또 내가 원하는 내용이 떴는지 확인
    wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div#boxoffice_list_content li.boxoffice_li')))
    time.sleep(2)
    
    get_movie_list()
    
# 미션1. 모든 페이지 영화 목록 다 가져오기 
# 1. 2페이지 이동한다
# 2. 2페이지의 내용을 다시 다 출력한다

# 3. 어?? 복붙했네.. 함수를 만든다
# 4. 함수에 저 페이지 번호를 인자값으로 준다??
# 5. 1~10페이지까지 모든 내용 다 가져온다...

print(data)

print('-'*50)

my_db.query_movie(cur)

# 연결 종료
my_db.close_db(conn)

# 미션2. 가져온 내용 우리 DB에 넣기
# 1. 디비 테이블 생성한다. (스키마 설계하기)
# 2. 위에 리스트에 있는 내용을 DB에 삽입한다. (SQL 쿼리문...)

# 브라우저 닫기
driver.quit()
