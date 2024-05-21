users = [
    {"name": "Alice", "age": 25, "location": "Seoul", "car": "BMW"},
    {"name": "Alice", "age": 30, "location": "Jeju", "car": "K5"},
    {"name": "Bob", "age": 30, "location": "Busan", "car": "Mercedes"},
    {"name": "Charlie", "age": 35, "location": "Daegu", "car": "Audi"},
]

print(users)

# def find_user(name):
#     # 입력받은 사용자 정보를 출력하시오.
#     for u in users:
#         if u['name'].lower() == name.lower():
#             print(f'검색결과 {u}')
#             return u
        
#     print(f'찾으시는 {name} 가 없습니다.')
        
# name = input('검색할 이름을 입력하세요: ')


# find_user(name)

# ===================================================
def find_user(name):
    # 입력받은 사용자 정보를 출력하시오.
    find_users = []
    for u in users:
        if u['name'].lower() == name.lower():
            find_users.append(u)

    return find_users
        
name = input('검색할 이름을 입력하세요: ')

found = find_user(name)
print(f'찾은 사람: {found}')