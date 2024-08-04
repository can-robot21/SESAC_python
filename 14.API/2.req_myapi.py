from my_jsonplaceholder_api import JSONPlaceHolderAPI

# 해당 클래스 초기화 

api = JSONPlaceHolderAPI()

user_posts = api.get_posts_by_user(1)

for comment in user_posts:
    # print(comment)
    print(comment['title'])
    
post_comments = api.get_commments_by_post(1)
for commet in post_id:
    print(comment['title'])