from flask import SQLAlchemy

# Flask - SQLAchemy 연결
# 일단 비워둠
db = SQLAlchemy

# 클래스를 통해서 DB 테이블을 설계/설정 할 수 있음.
class Sesac(db.model):
    __tablename__ = 'users' # 옵셔널 한것. 테이블명이 클래스명과 다를때 설정함.
    id = db.Column(db.Integer, primary_key=True) # PRIMAY KEY
    name = db.Column(db.Sting, nullable=False) #VARCHAR(20), NOT NULL
    age = db.Column(db.Integer, nullable=True)
    
    def __repr__(self): # 나의 객체를 누군가 print 할때, 표현해주고 싶은 함수를 구현
        return f'<사용자 {self.name}'