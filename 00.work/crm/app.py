from flask import Flask, render_template, redirect, request, url_for
import sqlite3, math
from database import get_db_connect, create_tables

app = Flask(__name__)

DATABASE = 'newcrmdb.db'
PER_PAGE = 20
START_PAGE = 1
PER_LIST = 15

def detail(dbname, id):
    conn = get_db_connect()
    cur = conn.cursor()
    
    query = f'SELECT * FROM {dbname} WHERE id = ?'
    cur.execute(query, (id,))
    row = cur.fetchone()
    columns = [desc[0] for desc in cur.description]  # 컬럼 이름 추출
    
    # row 데이터와 컬럼 이름을 딕셔너리 전환
    info = dict(zip(columns, row))
    return info

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
    user_info = detail("users", user_id)
    
    return render_template('detail.html', info=user_info)
      
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

@app.route('/detail_store/<store_id>')
def detail_store(store_id):
    store_info = detail("stores", store_id)
    
    return render_template('detail.html', info=store_info)

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

@app.route('/detail_item/<item_id>')
def detail_item(item_id):
    item_info = detail("items", item_id)
    
    return render_template('detail.html', info=item_info)

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

@app.route('/detail_order/<order_id>')
def detail_order(order_id):
    order_info = detail("orders", order_id)
    
    return render_template('detail.html', info=order_info)

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

@app.route('/detail_orderitem/<orderitem_id>')
def detail_orderitem(orderitem_id):
    orderitem_info = detail("orderitems", orderitem_id)
    
    return render_template('detail.html', info=orderitem_info)

if __name__ == "__main__":
    create_tables()
    app.run(debug=True, port=5500)
