import Flask import flask

# DB 모델 정의
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    age = db.Column(db.Integer)
    
# 초기화
with app.app_context():  
    db.create_all()
    
    # 새로운 사용자 계정
    new_user = User(name='user1', age=30)
    db.session.add(new_user)
    new_user2 = User(name='user2', age=19)  
    db.session.add(new_user2)
    db.session.commit() 