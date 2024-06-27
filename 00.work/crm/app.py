from flask import Flask, render_template, redirect, request, url_for
import sqlite3, math
from database import get_db_connect, create_tables

app = Flask(__name__)

DATABASE = 'newcrmdb.db'
PER_PAGE = 20


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return f'기능 추가 예정'

@app.route('/sign')
def sign():
    return f'기능 추가 예정'

@app.route('/user')
@app.route('/user/<int:page>')
def user(page=1):
    name_query = request.args.get('name', '').lower().strip()
    
    conn = get_db_connect()
    cur = conn.cursor()
    
    if name_query:
        query = 'SELECT * FROM users WHERE LOWER(name) LIKE ?'
        cur.execute(query, ('%'+name_query+'%',))
    else:
        query = 'SELECT * FROM users'
        cur.execute(query)
        
    rows = cur.fetchall()
    # 헤더 및 데이터 처리
    if rows:        
        headers = rows[0]
        rows = rows[1:]
        
    total_page = math.ceil(len(rows) / PER_PAGE)
    start_index = (page-1) * PER_PAGE
    end_index = start_index + PER_PAGE
    users  = rows[start_index:end_index]
    
    return render_template('user.html', headers=headers, users=users, total_page=total_page, now_page=page, name_query=name_query)
    
@app.route('/store')
@app.route('/store/<int:page>')
def store(page=1):
    name_query = request.args.get('name', '').lower().strip()
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
    
    total_page = math.ceil(len(rows) / PER_PAGE)
    start_index = (page - 1) * PER_PAGE
    end_index = start_index + PER_PAGE
    stores = rows[start_index:end_index]
    
    conn.close()
    return render_template('store.html', headers=headers, stores=stores, total_page=total_page, now_page=page, name_query=name_query)

@app.route('/item')
@app.route('/item/<int:page>')
def item(page=1):
    conn = get_db_connect()
    cur = conn.cursor()
    query = 'SELECT * FROM items'
    rows = cur.execute(query).fetchall()
    
    # 해더 및 데이터 처리
    if rows:
        headers = rows[0].keys()
        rows = rows[1:]
        
        items = rows[(page - 1) * PER_PAGE: page * PER_PAGE]
        total_page = math.ceil(len(rows)/PER_PAGE)    
    
    return render_template('item.html', headers=headers, total_page=total_page, now_page = page, items=items)

@app.route('/order')
@app.route('/order/<int:page>')
def order(page=1):
    conn = get_db_connect()
    cur = conn.cursor()
    query = 'SELECT * FROM orders'
    rows = cur.execute(query).fetchall()
    
    # 해더 및 데이터 처리
    if rows:
        headers = rows[0].keys()
        rows = rows[1:]
        
        orders = rows[(page-1)*PER_PAGE: page*PER_PAGE]
        total_page = math.ceil(len(rows)/PER_PAGE)
        
    return render_template('order.html', headers=headers, total_page=total_page, now_page=page, orders=orders)

@app.route('/orderitem')
@app.route('/orderitem/<int:page>')
def orderitem(page=1):
    conn = get_db_connect()
    cur = conn.cursor()
    query = 'SELECT * FROM orderitems'
    rows = cur.execute(query).fetchall()
    
    # 해더 및 데이터 처리
    if rows:
        headers = rows[0].keys()
        rows = rows[1:]
        
        orderitems = rows[(page-1) * PER_PAGE : page * PER_PAGE]
        total_page = math.ceil(len(rows)/PER_PAGE)
        
    return render_template('orderitem.html', headers=headers, total_page=total_page, now_page=page, orderitems=orderitems)
    
    
if __name__ == "__main__":
    create_tables()
    app.run(debug=True, port=5500)