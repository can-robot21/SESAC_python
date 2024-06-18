from flask import Flask, session

app = Flask(__name__)

app.secret_key = 'this-is-my-secret' # 세션 데이터 암호키

@app.route('/')
def index():
    # 세션에 데이터 저장
    session['username'] ="user1234"
    session['data'] ="user1234"
    return "핼로우"

@app.route('/get_session')
def get_session_data():
    username = session.get('username')
    data = session.get('data')
    
    return f"사용자이름: { username }, 데이터 : { data }"

if __name__ == "__main__":
    app.run(debug=True)
    