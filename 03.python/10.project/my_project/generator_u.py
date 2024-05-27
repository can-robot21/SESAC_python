import random
import uuid
import csv

# 이름조합을 위한 데이터셋 호출

# 성+중간+마지막 조합

# 입력받은 숫자 만큼의 이름 조합후 파일 출력과 name+날짜 조합으로 csv 파일로 저장
name1 = ['김', '이', '박', '최', '윤', '서', '강', '양', '정', '조', '장', '임' ]
name2 = ['민준', '서준', '예준', '도윤', '시우', '주원', '하준', '지호', '지후', '준서', '준우', '현우', '도현', '지훈', '건우', '서연', '서연', '지우', '서현', '민서', '하은', '하윤', '윤서', '지유', '지민', '채원', '지윤', '은서', '수아', '다은']
cities = ['서울시 동대문구', '서울시 서대문구', '서울시 종로구', '서울시 중구', '서울시 광진구', '경기도 성남시', '경기도 부천시', '경기도 남양주시', '경기도 구리시', '인천시 남동구', '인천시 서구', '인천시 부평구', '인천시 남동구']
streets = ['느티로 2', '금강로 333', '산마루로 24', '중앙로 245', '세종로 14', '통이로 135', '경기대로 13', '충정로 11길', '신촌로 223', '왕산로 239', '제기로 117', '천호대로 21']



def name_generate(int_name):
    user_name = []
    
    for i in range(int_name):
        new_name = random.choice(name1)+random.choice(name2)
        user_name.append(new_name)
    return user_name

def id_generate(int_id):
    user_id = []
    
    for i in range(int_id):
        user_id.append(str(uuid.uuid4()))        
    return user_id

def gender_generate(int_gender):
    gender = ['male', 'female']
    user_gender = []
    
    for i in range(int_gender):
        user_gender.append(random.choice(gender))        
    return user_gender

def birthdate_generate(int_birthdate):
    users_birthdate = []
    
    for i in range(int_birthdate):
        year = random.randint(1970, 2010)
        month = random.randint(1, 12)
        day = random.randint(1, 28)
        age = 2024 - year
        new_birthdate = f"{year}-{month:02d}-{day:02d}"
        users_birthdate.append((new_birthdate, age))
        
    return users_birthdate 

def address_generate(int_address):
    users_address = []
    
    for i in range(int_address):
        new_address = cities[random.randint(0, len(cities)-1)]+streets[random.randint(0,len(streets)-1)]
        users_address.append(new_address)
        
    return users_address
        
def random_users(users_number):
    name_data = name_generate(users_number)
    id_data = id_generate(users_number)
    gender_data = gender_generate(users_number)
    birthdate_data = birthdate_generate(users_number)
    address_data = address_generate(users_number)
    
    print('이름 데이터: ', name_data)
    print('회원 아이디: ', id_data)
    print('셩별 데이터', gender_data)
    print("생년월인: ", birthdate_data)
    print("생성 주소: ", address_data)
    
    users_data = []
    
    for i in range(users_number):
        new_user = (id_data[i], name_data[i], gender_data[i], *birthdate_data[i], address_data[i])
        users_data.append(new_user)
        print(new_user)
        
    print("생성 결합된 유저데이터: ", users_data)
    return users_data    

users_number = int(input("생성 유저수: "))
data=random_users(users_number)

print('파일로 저장 >>')
with open('user_data.txt', 'w', encoding='utf-8') as file:
    writer = csv.writer(file)
    for u in data:
        writer.writerow(u)
