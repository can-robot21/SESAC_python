from flask import Flask, render_template, jsonify
import sqlite3

app = Flask(__name__)

DATABASE = './newcrmdb.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # This allows us to return rows as dictionaries
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM users LIMIT 20')
    stores = cur.fetchall()
    conn.close()
    
    return render_template('index.html', stores=stores)

@app.route('/user', methods=['GET'])
def get_users():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM users')
    rows = cur.fetchall()
    conn.close()
    
    # Convert rows to list of dictionaries
    users = [dict(row) for row in rows]
    
    return jsonify(users)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5500)
