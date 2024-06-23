from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  

# flask-sqlalchemy 설정
db = SQLAlchemy(app)

# DB 모델 정의
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    age = db.Column(db.Integer)
    
# 초기화
with app.app_context():  
     db.create_all()
    
@app.route('/add', methods = ['POST'])
def add():
    name = request.form.get('name')
    age = request.form.get('age')
    
    new_user = User(name=name, age=int(age))
    db.session.add(new_user)
    db.session.commit()
    
    return redirect(url_for('home'))
    


@app.route('/')
def home():
    users = User.query.all() 
    return render_template('index.html', users = users)
 
    
if __name__ == "__main__":
    app.run(debug=True, port=5500)
