from flask import Flask, render_template
from flask import request, jsonify

app = Flask(__name__)

users = [
    { 'name': 'bill', 'age': 25, 'phone' : '123-456-1234'},
    { 'name': 'jane', 'age': 30, 'phone' : '010-456-0000'},
    { 'name': 'kim', 'age': 22, 'phone' : '234-444-1212'},
    { 'name': 'kim', 'age': 30, 'phone' : '234-444-4444'}
    ]

@app.route('/')
def main():
    result = render_template('index2.html', users = users)
    return result

@app.route('/user')
def get_user_by_name():
    search_name = request.args.get("name")
    search_age = request.args.get("age")
    print(search_name)
    print(search_age)
    
    search_result = users
    
    if search_name:
        search_result = [i for i in search_result if i['name'] == search_name]
        
    if search_age:
        search_result = [i for i in search_result if i['age'] == int(search_age)]

        
    return render_template("index2.html", users=search_result)


if __name__ == "__main__":
    app.run(debug=True)