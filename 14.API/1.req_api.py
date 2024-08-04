import requests

# 외부에 요청
user_id = 1
url = f'https://jsonplaceholder.typicode.com/posts?userId={user_id}'

response = requests.get(url)
post_data = response.json()
for comment in response:
    print('첫번째:', comment)
    # print('title:', comment['title'])

print('-'*20)

# 2 게시글 ID  기준으로 댓글
post_id = 1

url = f'https://jsonplaceholder.typicode.com/posts/{post_id}'

response = requests.get(url)
post_data = response.json()
for comment in response:
    print('두번째:', comment)
    # print('title:', comment['title'])
