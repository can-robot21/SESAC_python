import random
import uuid
import csv
from generator_address import generate_address
from print import printData

# 스토어 데이터 생성기
# stor_data : id, name, type, address
names = ['신촌점', '잠실점', '송도점', '토평점', '강남점', '양평점', '운정점', '대학로점', '시청점', '박다방', '꽁짜', '중앙점', '시티점']
types = ['스타벅스', '이디야', '투썸']

def stores_generator(num_stores):
    stores_data = []
    
    for i in range(num_stores):
        store_id = str(uuid.uuid4())
        store_name = random.choice(names)
        store_type = random.choice(types)
        store_address = generate_address()
        
        store_data = [
            store_id,
            store_name,
            store_type,
            store_address
        ]
        stores_data.append(store_data)
        
    return stores_data

    
# [파일저장]이나 [파일저장 & 화면출력] 선택 처리   

if __name__ == "__main__":
        
    num_stores = int(input('생성할 매장수: '))
    data = stores_generator(num_stores)

    print("s", data)