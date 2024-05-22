users = [
    {"name": "Alice", "age": 25, "location": "Seoul", "car": "BMW"},
    {"name": "Alice", "age": 30, "location": "Jeju", "car": "K5"},
    {"name": "Bob", "age": 30, "location": "Busan", "car": "Mercedes"},
    {"name": "Bob", "age": 28, "location": "Busan", "car": "Mercedes"},
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
# def find_user(name, age):
#     # 입력받은 사용자 정보를 출력하시오.
#     find_users = []
#     print(len(name), len(age))
#     for u in users:
        
#         if len(name)==0 and len(age)==0:
#             find_users=users
#         elif u['name'].lower() == name.lower() or u['age'] == age:
#             find_users.append(u)

#     return find_users
        
# name = input('검색할 이름을 입력하세요: ')
# age = input('나이: ')

# found = find_user(name, age)
# print(f'찾은 사람: {found}')

# 미션1. name + age
# 미션2. name or age

def display_user(users):
    print('-------------- 찾은 사용자 목록 ---------------')
    if len(users) == 0:
        print(users)
    
    

def find_user(name=None, age=None):
    found_user = []
    print(f'이름 {name} 나이 {age}')
    if name is None and age is None:
        return users
    else:
        for u in users:
            print(f'이름: {["name"]} 나이: {["age"]} 사는 곳: {["location"]}')
    
    for u in users:
        # 이름 나이 모두 있음
        if name is not None and age is not None:
            if u["name"].lower() == name.lower() and u["age"] == age:
                found_user.append(u)
            
        # 이름만 있음
        elif name is not None:
            if u["name"].lower() == name.lower():
                found_user.append(u)
            
        # 나이만 있음
        elif age is not None:
            if u["age"] == age:
                found_user.append(u)

    return found_user

found = find_user('alice')
display_user(found)


def find_user2(search):
    result = []

    for u in users:
        # 조건문 적절하게 넣기
        if (search.get('name') is None or u.get('name') == search.get('name')) and \
           (search.get('min_age') is None or u.get('age') >= search.get('min_age')) and \
           (search.get('location') is None or u.get('location') == search.get('location')) and \
           (search.get('car') is None or u.get('car') == search.get('car')):
            
            result.append(u)
        
    return result
        

search_criteria1 = {"name": "Bob"}
search_criteria2 = {"name": "Alice", "age": 30}
# search_criteria2 = {"name": "Alice"}
search_criteria3 = {"location": "Jeju", "car": 'BMW'}
search_criteria4 = {"location": "Jeju", "car": 'K5'}
search_criteria5 = {"name": "Alice", "min_age": 20}
search_criteria6 = {"name": "Alice", "min_age": 30}


print(find_user2(search_criteria6))

def find_user3(search):
    result = []
    
    for user in users:
        if match_criteria(user, search):
            result.append(user)
            
    return result

def match_criteria(user, criteria):
    for key, value in criteria.items():  # 딕셔너리 안에 있는 k, v 쌍을 하나씩 추출
        if key == "age":
            if user["age"] != value:
                return False
        if key == "name":
            if user["name"] != value:
                return False
        if key == "location":
            if user["location"] != value:
                return False
        if key == "car":
            if user["car"] != value:
                return False
    
    return True  
print('다른 함수: ')      
print(find_user3(search_criteria5))