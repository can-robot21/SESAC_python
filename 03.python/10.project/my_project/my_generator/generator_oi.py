import csv
import uuid
import random
00
# 주문정보와 상품(items) CSV 에서 읽어 생성
# ID + 날짜로 주문아아템 생성 후 저장

def list_orderItem(num_oi):
    orderItems = [[],[]]
    list_oi = []
    file = ['data_orders.csv', 'data_items.csv']
    
    # 파일에서 id만 읽기
    for i in range(2):
        print(i, file)
        with open(file[i], 'r', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=',')
            for row in reader:
                # 읽은 행이 비어있지 않은 경우에만 추가
                if row:
                    orderItems[i].append(row[0])
                
    print('list1:', orderItems[0])
    print('list2:', orderItems[1])
    
    for oi in range(num_oi):
        selected_order = random.choice(orderItems[0])
        selected_item = random.choice(orderItems[1])
        orderItem_Id = str(uuid.uuid4())
        
        list_oi.append[orderItem_Id, selected_order, selected_item]  
        
    return list_oi

def print_orderItem(print_set):
    if print_set == 1: # CSV 파일 저장 및 화면 출력
        with open('data_orderItems.csv', 'w', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerrow(['orderItem_Id', 'order_id', 'item_id'])
            writer.writerrows(data)
        print("CSV 저장 완료")
    elif print_set == 2: # CSV 파일 저장 및 화면 출력
        with open('data_orders.csv', 'w', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['orderItem_id', 'order_id', 'item_id'])
            writer.writerows(data)
        print('CSV 저장 및 출력 완료')
        for orderItem in data:
            print(orderItem)
            
            

num_oi = int(input("데이터 생성할 oderItem 숫자를 입력하세요.: "))
print_set = int(input('출력 모드를 선택:(1. CSV 파일저장 2. CSV 파일 및 화면출력): '))
data = list_orderItem(num_oi)
print_orderItem(print_set)

