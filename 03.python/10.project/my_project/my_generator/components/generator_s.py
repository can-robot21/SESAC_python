import random
import uuid
import csv

# 스토어 데이터 생성기
# stor_data : id, name, type, address
names = ['스타벅스 신촌점', '스타벅스 잠실점', '스타벅스 송도점', '스타벅스 토평점', '투썸 강남점', '투썸 양평점', '투썸 운정점', '카페 나무늘보', '크리미 카페', '박다방', '꽁차', '슈퍼맨', '메가시티']
types = ['스타벅스', '개인', '투썸']
cities = ['서울시 동대문구', '서울시 서대문구', '서울시 종로구', '서울시 중구', '서울시 광진구', '경기도 성남시', '경기도 부천시', '경기도 남양주시', '경기도 구리시', '인천시 남동구', '인천시 서구', '인천시 부평구', '인천시 남동구']
streets = ['느티로 2', '금강로 333', '산마루로 24', '중앙로 245', '세종로 14', '통일로 135', '경기대로 13', '충정로 11길', '신촌로 223', '왕산로 239', '제기로 117', '천호대로 21']

def stores_generator(num_stores):
    stores_data = []
    
    for i in range(num_stores):
        store_id = str(uuid.uuid4())
        store_name = random.choice(names)
        store_type = random.choice(types)
        store_address = random.choice(cities)+' '+random.choice(streets)
        
        store_data = [
            store_id,
            store_name,
            store_type,
            store_address
        ]
        stores_data.append(store_data)
        
    return stores_data

    
# [파일저장]이나 [파일저장 & 화면출력] 선택 처리   
def print_stores(mode):
    if mode == "1":
        # 유저파일 저장
        with open('data_stores.txt', 'w', encoding='utf-8') as file:
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
    
num_stores = int(input('생성할 매장수: '))
data = stores_generator(num_stores)

mode = input('[1] 매장 데이터 저장 [2] 매장 데이터 저장&화면출력, Mode 선택 [1] or [2]: ')
print_stores(mode)