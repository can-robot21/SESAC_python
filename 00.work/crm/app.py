from flask import Flask, render_template, redirect, request, url_for
import sqlite3, math
from database import get_db_connect, create_tables

app = Flask(__name__)

DATABASE = 'newcrmdb.db'
PER_PAGE = 20
START_PAGE = 1
PER_LIST = 15


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
    
    if rows:        
        headers = rows[0]
        rows = rows[1:]
    
    total_page = math.ceil(len(rows) / PER_PAGE)
    start_index = (page-1) * PER_PAGE
    end_index = start_index + PER_PAGE
    users  = rows[start_index:end_index]   
    
    start_page = ((page - 1) // PER_LIST) * PER_LIST + 1
    
    return render_template('user.html', users=users, total_page=total_page, now_page=page, name_query=name_query, start_page=start_page, per_list=PER_LIST, min=min)

@app.route('/detail_user/<user_id>')
def detail_user(user_id):
    conn = get_db_connect()
    cur = conn.cursor()
    
    query = 'SELECT * FROM users WHERE id = ?'
    cur.execute(query, (user_id,))
    row = cur.fetchone()
    print(f'사용자 ID {user_id}의 검색결과: {row}')
    
    return render_template('detail_user.html', user_info=row)
      
@app.route('/store')
@app.route('/store/<int:page>')
def store(page=1):
    name_query = request.args.get('name', '').lower().strip()
    
    conn = get_db_connect()
    cur = conn.cursor()
    
    if name_query:
        query = 'SELECT * FROM stores WHERE LOWER(name) LIKE ?'
        cur.execute(query, ('%' + name_query + '%',))
    else:
        query = 'SELECT * FROM stores'
        cur.execute(query)
        
    rows = cur.fetchall()
    
    # 헤더처리
    if rows:        
        headers = rows[0]
        rows = rows[1:]
    
    total_page = math.ceil(len(rows) / PER_PAGE)
    start_index = (page-1) * PER_PAGE
    end_index = start_index + PER_PAGE
    stores  = rows[start_index:end_index]   
    
    start_page = ((page - 1) // PER_LIST) * PER_LIST + 1
    
    conn.close()
    return render_template('store.html', stores=stores, total_page=total_page, now_page=page, name_query=name_query, start_page=start_page, per_list=PER_LIST, min=min)

@app.route('/item')
@app.route('/item/<int:page>')
def item(page=1):
    conn = get_db_connect()
    cur = conn.cursor()
    query = 'SELECT * FROM items'
    rows = cur.execute(query).fetchall()
    
    # 헤더처리
    if rows:        
        headers = rows[0]
        rows = rows[1:]
    
    total_page = math.ceil(len(rows) / PER_PAGE)
    start_index = (page - 1) * PER_PAGE
    end_index = start_index + PER_PAGE
    items = rows[start_index:end_index]
    
    start_page = ((page - 1) // PER_LIST) * PER_LIST + 1
    
    return render_template('item.html', items=items, total_page=total_page, now_page=page, start_page=start_page, per_list=PER_LIST, min=min)

@app.route('/order')
@app.route('/order/<int:page>')
def order(page=1):
    conn = get_db_connect()
    cur = conn.cursor()
    query = 'SELECT * FROM orders'
    rows = cur.execute(query).fetchall()
    
    # 헤더처리
    if rows:        
        headers = rows[0]
        rows = rows[1:]
    
    total_page = math.ceil(len(rows) / PER_PAGE)
    start_index = (page - 1) * PER_PAGE
    end_index = start_index + PER_PAGE
    orders = rows[start_index:end_index]
    
    start_page = ((page - 1) // PER_LIST) * PER_LIST + 1
    
    return render_template('order.html', orders=orders, total_page=total_page, now_page=page, start_page=start_page, per_list=PER_LIST, min=min)

@app.route('/orderitem')
@app.route('/orderitem/<int:page>')
def orderitem(page=1):
    conn = get_db_connect()
    cur = conn.cursor()
    query = 'SELECT * FROM orderitems'
    rows = cur.execute(query).fetchall()
    
    # 헤더처리
    if rows:        
        headers = rows[0]
        rows = rows[1:]
    
    total_page = math.ceil(len(rows) / PER_PAGE)
    start_index = (page - 1) * PER_PAGE
    end_index = start_index + PER_PAGE
    orderitems = rows[start_index:end_index]
    
    start_page = ((page - 1) // PER_LIST) * PER_LIST + 1
        
    return render_template('orderitem.html', orderitems=orderitems, total_page=total_page, now_page=page, start_page=start_page, per_list=PER_LIST, min=min)

if __name__ == "__main__":
    create_tables()
    app.run(debug=True, port=5500)
