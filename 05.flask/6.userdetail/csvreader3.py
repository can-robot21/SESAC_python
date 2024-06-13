import csv
import math
from flask import Flask, render_template
from flask import request

app = Flask(__name__)

csv_data = []

def load_csv_data(filename):
    global headers #글로벌 변수 : 바깥 변수를 내부에서 수정할 경우 선언함
    with open(filename, newline='', encoding='utf8') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        headers = csv_reader.fieldnames
        for row in csv_reader:
            clean_row = {fieldname.strip(): value.strip() for fieldname, value in row.items()}
            csv_data.append(clean_row)

@app.route("/")
@app.route("/<int:page>")
def index(page=1):
    per_page = 20  
    
    total_pages = math.ceil(len(csv_data) / per_page)
    start_index = (page - 1) * per_page
    end_index = start_index + per_page
    users = csv_data[start_index:end_index]
    # current_page = {} // 현재 페이지와 데이터 정리
    # print(f" 데이터 내용: {users}")
    # 필터링된 데이터를 기반으로 템플릿 렌더링
    return render_template("index3.html", headers=headers, users=users, total_pages=total_pages)

@app.route('/user/{uuid}')
def search(uuid):
    uuid_query = request.args.get(uuid)
    users = csv_data
    
    print(f"검색할 UUID: { uuid_query }")
    
    if uuid_query:
        filtered_users = [ user for user in users if user['Id'] == uuid_query ]
    else:
        filtered_users = users
        
    users = filtered_users
        
    print(f"검색된 사용자: {filtered_users}")
    return render_template("user.html", users)
    

if __name__ == '__main__':
    load_csv_data('./user.csv')
    # print(csv_data)
    app.run(debug=True)