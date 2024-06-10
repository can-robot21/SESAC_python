from flask import Flask, jsonify

app = Flask(__name__)

users = [
    { "name": "Alise", "age": 27, "phone": "123-234-3456" },
    { "name": "Charlie", "age": 33, "phone": "234-456-0022"},
    { "name": "Jane", "age": 22, "phone": "234-456-0022"},
    { "name": "Kim", "age": 30, "phone": "234-456-0022"}     
]

@app.route("/")
def home():
    return jsonify(users)

@app.route("/user/<name>")
def search_user(name):
    user = None
    # 유저에 name 이 있을 경우 찾아서 반납
    name = name
    for i in users:
        if i["name"] == name:
            user = i
        if str(i["age"]) == name:
            user = i

    return jsonify({'error': 'User not Found'}), 404
    if user:
        return jsonify(user), 200
    else:
        return jsonify(user), 404 
    

if __name__ == "__main__":
    app.run(debug=True)