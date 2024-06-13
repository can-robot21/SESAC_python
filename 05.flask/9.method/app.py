from flask import Flask, render_template, request
users = [
    {'name': 'Alice', 'id': 'Alice', 'password': 'Alice'},
    {'name': 'Tom', 'id': 'Tom', 'password': 'Tom'},
    {'name': 'Jane', 'id': 'Jane', 'password': 'Jane'} 
]

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def home():
    user = None
    id = request.args.get('id') # GET 방식의 URL 파라미터를 처리할때만 가능...
    
    if request.method == "POST":
        id = request.form['id'] # 포스트 방식 중에서 Form=Data 를 처리할때 PayLoad 를 받는다.
        pw = request.form['password']   
        
        # user = None
        # for u in users:
        #     if u['id'] == id and u['password'] == pw:
        #         print('  매치되는 사용자 있음  ')
        #         user = u
        
        user = next(( user for user in users if user['id'] == id and user['password'] == pw), None)       
        
                

        # 입력한 user 목록과 입력한 id/pw 비교해 print 로 로그인 여부 출력    
        print(f'입력한 ID: {id}, 입력한 PW: {pw}')
        
        if user:
            print(f"로드인한 사용자는 {user['name']}입니다.")
        else:
            print(f'로그인 가능한 사용자는 없습니다. id = {id}')
            message = "success!!"
        return render_template('index.html', user = user)

    return render_template('index.html', user = user)

if __name__ == "__main__":
    app.run(debug=True)
