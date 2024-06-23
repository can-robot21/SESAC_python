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
# chrome_options.add_argument("--no-sandbox")
# chrome_options.add_argument("--disable-dev-shm-usage")

# 크롬드라이버 초기화
service = Service(executable_path="./chromedriver.exe")
driver = webdriver.Chrome(service=service)

# 웹페이지 열기
driver.get('https://www.naver.com')

# 검색창에서 글자 입력하기
search_box = driver.find_element(By.NAME, 'query')
search_box.send_keys("Python programming")
search_box.send_keys(Keys.RETURN)

time.sleep(5)

# 결과 스크린샷
driver.save_screenshot('search_result_001.png')

# 브라우저 닫기
driver.quit()
