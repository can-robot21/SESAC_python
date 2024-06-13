from flask import Flask;

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello"

@app.route("/user/<name>")
def user(name):
    return f"Hello, {name}님!!"

@app.route("/user/<int:age>")
def userage(age):
    return f"<h2>Age: {age} </h2>"

@app.route("/user/<float:weight>")
def userweight(weight):
    return f"<h2>Weight: {weight} </h2>"

@app.route("/user/<name>/<age>/<weight>")
def usernameageweight(name, age, weight):
    return f"<h2>Name: {name}, Age: {age}, Weight: {weight} </h2>"

if __name__ == "__main__":
    app.run(debug=True)