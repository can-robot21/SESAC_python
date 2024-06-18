# from db_crud import create_table, insert_user, fetch_users, update_user, delete_user
import db_crud as db

# 메인 함수
def main():
    # 테이블 생성
    db.create_table()

    # 데이터 삽입
    db.insert_user("Alice", 30)
    db.insert_user("Bob", 25)
    db.insert_user("Charlie", 35)

    # 데이터 조회
    print("--- 데이터 조회 --- ")
    users = db.fetch_users()
    for user in users:
        print(user)
    print("--- 데이터 조회 끝 ---")
    
    # 데이터 수정
    db.update_user('Alice', 32)

    # 데이터 조회
    print("--- 엘리스 나이 변경 이후 --- ")
    users = db.fetch_users()
    for user in users:
        print(user)
    print("--- 데이터 조회 끝 ---")

    # 데이터 삭제
    db.delete_user('Bob')

    # 데이터 조회
    print("--- 밥 삭제 이후 --- ")
    users = db.fetch_users()
    for user in users:
        print(user)
    print("--- 데이터 조회 끝 ---")

if __name__ == "__main__":
    main()