from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

DATABASE = './newcrmdb.db'

@app.route('/')
def index():
    # 철자 오류 수정: connnect -> connect
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.execute('SELECT * FROM users LIMIT 20')
    stores = cur.fetchall()
    conn.close()
    
    return render_template('index.html', stores=stores)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5500)
