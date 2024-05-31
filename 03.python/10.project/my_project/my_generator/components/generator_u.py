import random
import uuid

# 성+이름 조합, 이름조합을 위한 데이터셋 호출
# 입력받은 숫자 만큼의 이름 조합후 파일 출력과 name+날짜 조합으로 csv 파일로 저장

def usersGenerate(num_users):
    users_data = []
    
    for i in range(num_users):
        year = random.randint(1970, 2010)
        month = random.randint(1, 12)
        day = random.randint(1, 28)
        birthdate=(f"{year}-{month:02d}-{day:02d}")
        age = 2024 - year
        
        # index 처리용
        user_id = str(uuid.uuid4())
        name = random.choice(name1)+random.choice(name2)
        gender = random.choice(gender_data)
        address = cities[random.randint(0, len(cities)-1)]+" "+streets[random.randint(0,len(streets)-1)]
        
        user_data = [            
            user_id,        
            name,
            gender,      
            birthdate,
            age,
            address
        ]
        
        users_data.append(user_data)
        
    return users_data   