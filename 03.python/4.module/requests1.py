# pip install requests

import requests

# 리퀘스트 모듈안에 있는 함수를 사용할 수 있음

# 1. 웹페이지에 있는 컨텐츠 가져올 수 있음
response = requests.get("https://jsonplaceholder.typicode.com/users")
print('웹 페이지 내용: ')
print(response)
print(response.status_code)
# print(response.text)

#
data = response.json()
# print("JSON 데이터: ", data)

users = data
for user in users:
    print("이름: {} ID: {}, 이메일: {}".format(user['name'], user['username'], user['email']))
