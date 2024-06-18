import sqlite3

# DB 연ㄱㄹ하기
conn = sqlite3.connect('example.db')

# 커서를 통한 데이터 입출력 포인터 가져오기
cur = conn.cursor()

# 커서통해 명령어 보내기
cur.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT not NULL,
                age INTEGER not NULL)
            ''')

# 커밋
conn.commit()

# 연결닫기
conn.close()