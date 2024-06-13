my_dict = {'name': 'Alice', 'age': 25, 'phone': '010-123-4567'}

# 빌트인 함수 = 내장 함수 
items = my_dict.items()
# print(list(items))  # type casting = 형 (  type ) 변환
items_list = list(items)

for item in items_list:
    print(item)
    
for key, value in items_list:
    print(f"key: {key}, value: {value}")
    
print('-' * 50)

for key, value in sorted(my_dict.items()):
    print(f"키: {key}, 값: {value}")

update_dict = {'car': 'K7', 'city': 'Seoul'}

# for key, value in update_dict.items():
    # my_dict[key] = value
    
print(f'원본: {my_dict}')
print(f'업데이트: {update_dict}')

new_dict = my_dict | update_dict # 3.9 이상의 python 에서 사용가능
print(f'통합본:  {new_dict}')

print('-' * 50)

users = [
    {'name': 'Alice', 'age': 25, 'phone': '010-123-4567'},
    {'name': 'Tom', 'age': 19, 'phone': '010-345-1212'},
    {'name': 'Charlie', 'age': 22, 'phone': '010-123-0000'}
]

filtered_user = []
for user in users:
    if user['age'] >= 20:
        filtered_user.append(user)
        
print(f'검색결과: {filtered_user}')

filtered_user = [user for user in users if user.get('age', 0) >= 20]
print(filtered_user)

filtered_user_age = [{key: value for key, value in u.items() if key == "age" and value >= 20} for u in users]
print(filtered_user_age)
        