from flask import Flask, jsonify
from flask import request

app = Flask(__name__)

users = [
    { "name": "Alise", "age": 27, "phone": "123-234-3456" },
    { "name": "Alise", "age": 30, "phone": "123-234-3456" },
    { "name": "Charlie", "age": 33, "phone": "234-456-0022"},
    { "name": "Jane", "age": 22, "phone": "234-456-1122"},
    { "name": "Kim", "age": 30, "phone": "234-456-0000"}     
]

@app.route("/")
def home():
    return jsonify(users)

@app.route("/search")
def search():
    name_query = request.args.get('name')
    age_query = request.args.get("age")
    phone_query = request.args.get("phone")
    result = users

    # return f"검색중: {query} on 페이지 {page}...", 200

    # 미션1. users 에서 query 구문이 name 인 사람 찾아 출력
    if name_query:
        result = [u for u in users if name_query.lower() in u['name'].lower()]
    # result = [u for u in users if age_query in str(u['age'])] 
    if age_query:
        result = [u for u in result if  age_query in str(u['age'])]
    if phone_query:
        result = [u for u in users if phone_query in u['phone'][-4:]]  
             
    return f" 이름 : { name_query }와 나이: { age_query } 일치하는 결과는 { result }입니다ㅏ."

    # 미션2. 나이로 검색
    # 미션3. 전화번호 끝자리 4자리 rjator
    
if __name__ == "__main__":
    app.run(debug=True)