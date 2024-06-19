from flask import Flask, render_template, request, session, redirect, url_for, flash
from datetime import timedelta
import database as db

app = Flask(__name__)
app.secret_key = 'hello1234'
app.permanent_session_lifetime = timedelta(minutes=5)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # 로그인 처리 구현
        username = request.form["username"]
        password = request.form["password"]

        # 사용자 데이터를 외부 DB에서 가져오기
        user_data = db.get_query("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        print(f"조회된 사용자: ", user_data)
        print([dict(row) for row in user_data])

        if len(user_data) == 1:  # and user_data["password"] == password
            session["user"] = user_data[0]["username"]
            if "email" in user_data[0]:
                session["email"] = user_data[0]["email"]
            session.permanent = True
            print("패스워드 맞음!!")
            flash("로그인에 성공하였습니다.")
            return redirect(url_for("home"))
        else:
            print('패스워드 틀림!!')
            flash("아이디/패스워드가 일치하지 않습니다.")
            return redirect(url_for("login"))
    else:
        # GET 요청이라서 로그인 폼 보여주기
        if "user" in session:
            print("이전에 로그인 했음!!")
            return redirect(url_for("home"))

    return render_template('login.html')

@app.route('/user', methods=['GET', 'POST'])
def user():
    if "user" in session:
        user = session['user']
        email = session.get('email', '')  # email이 세션에 없을 경우 기본값 '' 사용

        if request.method == "POST":
            email = request.form.get("email")
            password = request.form.get("password")

            if email:
                session['email'] = email
                db.execute_query("UPDATE users SET email=? WHERE username=?", (email, user))
            if password:
                db.execute_query("UPDATE users SET password=? WHERE username=?", (password, user))

            flash('프로필 업데이트 완료')

        return render_template('user.html', email=email)
    else:
        return redirect(url_for('login'))

@app.route('/view')
def view():
    users = db.get_query("SELECT * FROM users")
    return render_template("view.html", users=users)

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':        
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email', None)
        users = db.get_query('SELECT * FROM users')
        
        for user in users:
            if username == user[0]:
                print('동일한 username이 있습니다.')
                return redirect('signin')
        db.execute_query('INSERT INTO users (username, password, email) VALUES (?, ?, ?)', (username, password, email))
        print(f'새롭게  {{ username }} 님이 가입함, 이메일 {{ email }}')        
        flash(f'새롭게  {{ username }} 님이 가입함, 이메일 {{ email }}')    
        return redirect(url_for('login'))    
    
    return render_template('signin.html')

@app.route('/logout')
def logout():
    session.pop("user", None)
    session.pop("email", None)
    flash("로그아웃에 성공하였습니다.")
    return redirect(url_for("login"))

if __name__ == "__main__":
    db.init_db()  # 시스템 부팅 시에 DB 초기화
    print('DB 초기화 완료')
    app.run(debug=True, port=5500)  # 플라스크 앱 실행
