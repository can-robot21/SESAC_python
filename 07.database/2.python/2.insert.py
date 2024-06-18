import sqlite3

# DB에 연결하기
conn = sqlite3.connect('example.db')
cur = conn.cursor()

# 테이블에 데이터가 있는지 확인하기 위하 쿼리문
cur.execute('SELECT COUNT(*) FROM users')
count = cur.fetchone()[0]
print(f'현재 데이터 개수: ', count)

if count == 0:
    # 커서를 통해서 명령어 보내기
    cur.execute('INSERT INTO users (name, age) VALUES ("Alice", 30)')
    cur.execute('INSERT INTO users (name, age) VALUES (?, ?)', ('Bob', 25))
    
    # 커밋
    conn.commit()
else:
    print('데이터가 이미 있습니다.')

cur.execute('SELECT COUNT(*) FROM users')
count = cur.fetchone()[0]
print(f'종료시 데이터 개수: { count }')


# 연결닫기
conn.close()