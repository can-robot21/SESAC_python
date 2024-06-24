from flask import Flask, jsonify, send_from_directory, request
import sqlite3

app = Flask(__name__)

DATABASE = './newcrmdb.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def serve_index():
    return app.send_static_file('index.html')

@app.route('/api/stores')
def get_stores():
    name = request.args.get('name')
    conn = get_db_connection()
    cur = conn.cursor()
    
    if name:
        cur.execute('SELECT * FROM stores WHERE name LIKE ?', ('%' + name + '%',))
    else:
        cur.execute('SELECT * FROM stores LIMIT 20')
        
    rows = cur.fetchall()
    conn.close()
    
    stores = [dict(row) for row in rows]
    return jsonify(stores)

@app.route('/static/<path:path>')
def send_static_file(path):
    return send_from_directory('static', path)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5500)
