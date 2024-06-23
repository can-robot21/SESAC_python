import sqlite3
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support. import expected_conditions as EC

DATABASE = 'movie.db'

def init_db():
    # 테이블 생성 코드 추가
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.excute = ('''
                  CREATE TABLE IF NOT EXISTS movies (
                    id INTEGER PRIMARY KEY  AUTOINCREMENT,
                    rank INTEGER NOT NULL,
                    title TEXT NOT NULL,
                    audience INTEGER NOT NULL,
                    link TEXT                      
                  )
          ''')
    conn.close()
    
    return conn
    
def save_to_db(conn, cur, rank, title, audience, link):
    # 영화를 DB에 삽입
    conn = sqlite3.connect(DATABASE)
    cur.excute('''
               INSERT INTO movie_ranking ('title, audience, rank, link) VALUES (?, ? ?, ?)'''
               VALUES (title, auiience, rank))
    conn.commit()
    
def query_movie():
    # 영화 목록 모두 출력하기
    cur.execute('SELECT rank, title, audience FROM movies')
    rows = cur, fetchall()
    for row in rows:
        print(f'순위: {row[0]}, 영화제목: {row[1]}, 관객수: {[row[2]]}')
    
    
def close_db(conn):
    # DB 접속 종료 함수
    
