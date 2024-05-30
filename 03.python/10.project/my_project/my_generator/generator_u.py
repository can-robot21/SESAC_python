import random
import uuid
import csv

# 성+이름 조합, 이름조합을 위한 데이터셋 호출
# 입력받은 숫자 만큼의 이름 조합후 파일 출력과 name+날짜 조합으로 csv 파일로 저장
name1 = ['김', '이', '박', '최', '윤', '서', '강', '양', '정', '조', '장', '임' ]
name2 = ['민준', '서준', '예준', '도윤', '시우', '주원', '하준', '지호', '지후', '준서', '준우', '현우', '도현', '지훈', '건우', '서연', '서연', '지우', '서현', '민서', '하은', '하윤', '윤서', '지유', '지민', '채원', '지윤', '은서', '수아', '다은']
cities = ['서울시 동대문구', '서울시 서대문구', '서울시 종로구', '서울시 중구', '서울시 광진구', '경기도 성남시', '경기도 부천시', '경기도 남양주시', '경기도 구리시', '인천시 남동구', '인천시 서구', '인천시 부평구', '인천시 남동구']
streets = ['느티로 2', '금강로 333', '산마루로 24', '중앙로 245', '세종로 14', '통이로 135', '경기대로 13', '충정로 11길', '신촌로 223', '왕산로 239', '제기로 117', '천호대로 21']
gender_data = ['male', 'female']

def users_generate(num_users):
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

# [파일저장]이나 [파일저장 & 화면출력] 선택 처리   
def print_users(mode):
    if mode == "1":
        # 유저파일 저장
        with open('data_users.csv', 'w', encoding='utf-8') as file:
            writer = csv.writer(file)
            for u in data:
                writer.writerow(u)
        print('파일생성 완료')
    elif mode == "2":
        # 유저 파일저장 및 화면 출력
        with open('data_stores.csv', 'w', encoding='utf-8') as file:
            writer = csv.writer(file)
            for u in data:
                writer.writerow(u)
        print('파일저장 완료 저장 데이터 출력: ', data)
        for i in data:
            print(str(i))
    else:
        print('데이터 처리는 [1] 과 [2] 중 선택해 주세요.')

num_users = int(input("생성 유저수: "))
data=users_generate(num_users)

mode = input('[1] 유저데이터 저장 및 출력 [2] 유저데이터 파일생성 및 출력, [1] or [2] Mode 선택: ')
print_users(mode)