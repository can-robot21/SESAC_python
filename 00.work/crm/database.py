from flask import Flask, render_template, redirect, request, url_for
import sqlite3, math

DATABASE = './newcrmdb.db'

def get_db_connect():
    # DB 연결 및 row 데이터 생성
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def create_tables():
    # DB 생성 및 연결
    conn = get_db_connect()
    cur = conn.cursor()
    cur.execute('''
                CREATE TABLE IF NOT EXISTS "users"(
                    "Id" TEXT,
                    "Name" TEXT,
                    "Gender" TEXT,
                    "Age" INTEGER,
                    "Birthdate" DATE,
                    "Address" TEXT);                     
                ''')
    conn.commit()
    conn.close()
    
def get_user(page, name):
    per_page = 20
    name_query = name or request.args.get('name', '').lower().strip()
    
    conn = get_db_connect()
    cur = conn.cursor()
    
    if name_query:
        query = 'SELECT * FROM users WHERE LOWER(name) LIKE ?'
        cur.execute(query, ('%' + name_query + '%',))
    else:
        query = 'SELECT * FROM users'
        cur.execute(query)
        
    rows = cur.fetchall()
    total_page = math.ceil(len(rows) / per_page)
    start_index = (page-1) * per_page
    end_index = start_index + per_page
    users = rows[start_index:end_index]  # Paginated users
    
    conn.close()
    return render_template('user.html', users=users, total_page=total_page, now_page=page, name_query=name_query)

def get_store(page, name):
    per_page = 20
    name_query = name or request.args.get('name', '').lower().strip()
    # print('검색단어:', name_query)
    
    conn = get_db_connect()
    cur = conn.cursor()
    
        
    if name_query:
        query = 'SELECT * FROM stores WHERE LOWER(name) LIKE ?'
        cur.execute(query, ('%' + name_query + '%',))
    else:
        query = 'SELECT * FROM stores'
        cur.execute(query)
        
    rows = cur.fetchall()
    
    # 헤더 및 데이터 처리
    if rows:
        headers = rows[0]  # 첫 번째 행(헤더)을 headers 변수에 저장
        rows = rows[1:]    # 첫 번째 행을 제외한 나머지 데이터만 남깁니다.
    
    total_page = math.ceil(len(rows) / per_page)
    start_index = (page - 1) * per_page
    end_index = start_index + per_page
    stores = rows[start_index:end_index]
    
    conn.close()
    return render_template('store.html', headers=headers, stores=stores, total_page=total_page, now_page=page, name_query=name_query)
 