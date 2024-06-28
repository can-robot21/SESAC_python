from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, Sesac
import os

app = Flask(__name__)
app.secret_key = 'sesac1234'

DATABASE_NAME = 'example.db'
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DATABASE_NAME}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 해당 모듈을 불러온 이후, 초기화 함수를 통해 db - flask 연결
db.init_app(app)

@app.route('/')
def index():
    users = Sesac.query.all()
    # print(users)
    return render_template('index.html', users=users)

@app.route('/add_user', methods=["POST"])
def add_user():
    # GET 방식일때는 URL 파라미터를 통해 정보가 전달되고, args안에 담겨서 온다.
    # name = request.args.get('name')
    # age = request.args.get('age')
    # POST 방식일때는 BODY 안에 데이터가 담겨서 온다. 그 body 중에 우리가 보낸건 FORM 타입임
    name = request.form.get('name')
    age = request.form.get('age')
    print(f'입력값은: {name}, {age} 입니다.')

    if int(age) < 0:
        flash('나이는 음수일수 없습니다')
        return redirect(url_for('index'))

    if int(age) > 100:
        flash('나이는 100살보다 클 수 없습니다')
        return redirect(url_for('index'))

    new_user = Sesac(name=name, age=int(age))
    db.session.add(new_user)
    db.session.commit()
    flash(f"사용자{name}과 {age} 가 추가되었습니다.")

    # return f"<H1>사용자({name})가 추가되었습니다.</H1>"
    return redirect(url_for('index'))

@app.route('/update_user/<id>', methods=['POST'])
def update_user(id):
    user = db.session.get(Sesac, id)
    # if not user:
    #     flash('사용자가 없습니다')
    #     return redirect(url_for('index'))
    
    name = request.form.get('name')
    age = request.form.get('age')

    user.name = name
    user.age = int(age)
    if not name or not age:
        flash("이름과 나이는 빈칸일수 없습니다.")
        return redirect(url_for('edit_user', id=id))

    db.session.commit()

    flash(f'사용자{user.name} 정보를 업데이트 하였습니다.')
    return redirect(url_for('index'))

@app.route('/edit_user/<id>')
def edit_user(id):
    print(f"수정할 사용자 아이디는 {id} 입니다.")
    # 수정할 사용자 정보 가져와서, 뭘 어떻게 바꿀껀지 물어보기...
    user = db.session.get(Sesac, id)
    # if not user:
    #     flash("선택한 사용자가 없습니다???")
    #     return redirect(url_for('index'))
    
    return render_template('user_edit.html', user=user)
    # return "<H1>수정완료</H1>"

@app.route('/delete_user/<id>')
def delete_user(id):
    print(f"삭제할사용자 아이디는: {id}")
    # 삭제하는 코드 구현하기
    user = db.session.get(Sesac, id)
    if user:
        db.session.delete(user)
        db.session.commit()
        print(f"사용자가 {user.name} 삭제되었습니다.")
    else:
        print("사용자가 없습니다")

    # return "<H1>사용자 삭제함</H1>"
    return redirect(url_for('index'))

if __name__ == "__main__":
    with app.app_context():  # 우리의 app 즉 flask 앱이 초기화가 끝난 상태에서...
        db_path = os.path.join(app.instance_path, DATABASE_NAME)
        if not os.path.exists(db_path):
            db.create_all()
            print('DB가 없어서 새로 만들고 있음')

        if not Sesac.query.first():
            print('사용자가 없어서 새로 추가할것임...')
            # 만약, 초기화 할때, 사용자 데이터도 추가하고 싶으면???
            user1 = Sesac(name='user1', age=30)
            user2 = Sesac(name='user2', age=33)
            user3 = Sesac(name='user3', age=35)
        
            db.session.add(user1)
            db.session.add(user2)
            db.session.add(user3)
            db.session.commit()
            # 여기서의 세션은, 우리가 알고 있는 그 세션이 아님!!!!
            # 원작자(sqlalchemy를 만든사람) 이 DB 와 통신하는 그 방식(?)을 sessino 이라고 이름을 지었음

    app.run(debug=True)
