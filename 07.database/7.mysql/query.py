import pymysql

host = 'localhost'
user = 'sesac'
password = 'sesac'
database = 'sesac'

connection = pymysql.connect(
    host = host,
    user = user,
    password = password,
    database = database
)

cursor = connection.cursor()
cursor.execute("SELECT * FROM user")
results = curser.fetchall()
for res in results:
    print(res)