from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h2>Hello, Welcome to 내 플라스크 서버</h2><p> Home 첫페이지 </p>"

@app.route("/user/")
@app.route("/user/<name>")  # <name> 은 변수
def user(name=None):
    username = name

    return f"""<h2>여기는 사용자 {username} 님 안녕하세요. </h2><p> {username} 님의 소개 페이지입니다. </p>"""
@app.route("/admin")
def admin():
    return "<h2>관리자 페이지</h2><p> 관리자 페이지 </p>"

if __name__ == "__main__":
    app.run(debug=True) # 개발환경에서만 debug 사용, 배포서버에서는 상시 OFF