from flask import Flask, session, render_template, request, redirect, url_for

app = Flask(__name__)
app.secret_key = "startUp"

users = [
    {'name': 'Alice', 'id': 'Alice', 'password': 'Alice'},
    {'name': 'Tom', 'id': 'Tom', 'password': 'Tom'},
    {'name': 'Jane', 'id': 'Jane', 'password': 'Jane'} 
]


@app.route('/', methods =['GET', 'POST'])
def home():
    if request.method == "POST":
        id = request.form['id']
        pw = request.form['password']
        
        
        # 이사용자가 목록에 있음
        user = next(( user for user in users if user['id'] == id and user['password'] == pw), None)
        print(user)  
        if user:
            session['user'] = user  # 사용자 정보를 세션에 저장
            return redirect(url_for('profile'))  # 프로필 페이지로 리다이렉트
        else:
            return "로그인 실패"  # 로그인 실패 처리     
    
    return render_template("index.html")

@app.route('/profile')
def profile():
     # 세션에서 'user' 키로 저장된 사용자 정보를 가져옵니다. 없을 경우 기본값으로 지정된 사용자 정보를 사용합니다.
    user = session.get('user', {'name': '없음', 'id': '몰라', 'password': '역시 몰라'})
    
    # if POST 요청이 왔으면!!
    # 세션에서 user 정보 가져와  userDB 에서 검색 비교
    # pw 변경
    if request.method == "POST":
        new_pw = request.form['new_pw']
        for u in users:
            if u['id'] == user['id']:
                u['pw'] = new_pw
    
    return render_template('profile.html', user=user)  

@app.route('/logout')
def logout():
    session.pop('user', None) # 세션에서 User 정보 삭제
    return redirect(url_for('home')) # 로그아웃 후 돌아갈 페이지
    

if __name__ == "__main__":
    app.run(debug=True)