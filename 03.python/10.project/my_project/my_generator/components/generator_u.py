import random
from generator_name import generate_name
from generator_address import generate_address
from generator_id  import generate_uuid
from print import printData

# 성+이름 조합, 이름조합을 위한 데이터셋 호출
# 입력받은 숫자 만큼의 이름 조합후 파일 출력과 name+날짜 조합으로 csv 파일로 저장
name = generate_name()
gender_data = ['male', 'female']

def usersGenerate(num_users):
    users_data = []
    
    for i in range(num_users):
        year = random.randint(1970, 2010)
        month = random.randint(1, 12)
        day = random.randint(1, 28)
        birthdate=(f"{year}-{month:02d}-{day:02d}")
        age = 2024 - year
        user_id = generate_uuid()
        address = generate_address()
        
        # index 처리용
        gender = random.choice(gender_data)
        
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

# 메인 함수     
if __name__ == "__main__":
    num_users = int(input("사용자 데이터 생성 숫자는? "))
    data = usersGenerate(num_users)
    
    printData("u", data)