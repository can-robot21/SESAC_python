# ORM = Sql 를 대신하는 각각의 언어의 개발 코드

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///example.db')

# 원형
Base = declarative_base()

# 원형을 상속받아 테이블 설계
class User(Base):
    __tablename__ = 'users'  # 안할 경우 클래스명을 테이블명으로 사용됨
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    
# CREATE TABLE users (
#     id INTEGER PRIMARY,
#     name TEXT,
#     age INTEGER
# )

# 설계 실행
Base.metadata.create_all(engine)

# DB 입력출을 위한 세션메이커 사용
Session = sessionmaker(bind=engine)
session = Session()

# 이 session을 통해서 자유롭게 CRUD 가능함
new_user = User(name='Alice', age=30)
session.add(new_user)
session.commit()

new_user = User(name='Bob', age=22)
session.add(new_user)
session.commit()

# 사용자 조회
users = session.query(User).all()
for user in users:
    print(user.name, user.age)