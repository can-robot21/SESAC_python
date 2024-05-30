import csv
import uuid
import random
import datetime

# 유저 + 매장 CSV 파일 일어 조합
# ID + 날짜(생성) 추가해 주문정보 생성

def select_list(num_orders):    
    list_full = [[], []]
    list_select = []
    
    # 파일에서 id만 읽어오기
    with open('data_users.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            if row:  # 빈 줄이 아닌 경우에만 처리
                list_full[0].append(row[0])  # 유저 id만 저장

    with open('data_stores.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            if row:  # 빈 줄이 아닌 경우에만 처리
                list_full[1].append(row[0])  # 매장 id만 저장
            
    for i in range(num_orders):
        year = random.randint(2021, 2023)
        month = random.randint(1, 12)
        day = random.randint(1, 28)
        hour = random.randint(0, 23)
        minute = random.randint(0, 59)
        second = random.randint(0, 59)
        date = datetime.datetime(year, month, day, hour, minute, second)
        order_date = date.strftime('%Y-%m-%d %H:%M:%S')
        
        selected_user = random.choice(list_full[0])  
        selected_store = random.choice(list_full[1]) 
        order_id = str(uuid.uuid4()) 
        
        list_select.append((order_id, order_date, selected_user, selected_store))  # 주문 정보 추가
            
    return list_select


def print_order(print_set, data):
    if print_set == 1:  # CSV 파일 저장
        with open('data_orders.csv', 'w', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['order_id', 'order_date', 'user_id', 'store_id'])  # 헤더 추가
            writer.writerows(data)
        print("CSV 저장 완료")
    elif print_set == 2:  # CSV 파일 저장 및 화면 출력
        with open('data_orders.csv', 'w', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['order_id', 'order_date', 'user_id', 'store_id'])  # 헤더 추가
            writer.writerows(data)
        print("CSV 저장 및 출력 완료")
        for order in data:
            print(order)

num_orders = int(input('주문 생성 데이터 수: '))
print_set = int(input('생성 후 CSV 생성 및 파일 데이터 order_list 생성하기: 1 또는 2 선택: '))
data = select_list(num_orders)
print_order(print_set, data)
