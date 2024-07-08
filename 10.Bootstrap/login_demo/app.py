from flask import Flask, render_template, redirect, url_for, request, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'star1234'

# 사용자 계정정보
# users = {'username': 'password'}
DATABASE = 'users.db'

def connect_db():
    return sqlite3.connect(DATABASE)

def init_database():
    db = connect_db()
    cursor = db.cursor()
    cursor.execute('''
                   CREATE TABLE IF EXISTS users (
                       id INTEGER PRIMARY KEY AUTOINCREAMENT,
                       username TEXT UNIQUE NOT NULL,
                       password TEXT NOT NULL
                   )
                   ''')

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            print('사용자 로그인 성공')
            flash('로그인 성공.', 'success')
        else:
            print('로그인 실패')
            flash('로그인 실패. 사용자 이름 또는 패스워드를 올바르게 입력해 주세요.', 'danger')
    
    return render_template('login.html')

if __name__ == "__main__":
    app.run(debug=True)
