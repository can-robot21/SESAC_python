import random
import csv
import uuid

# 매장 아이템 juice, coffee, cake 
# 가격

item_type = ['COFFEE', 'JUICE', 'CAKE', 'BLEND']
item_name1 = ['아메리카노', '카페라떼', '에스프레소', '카푸치노', '모카라떼']
item_name2 = ['오렌지주스', '애플주스', '포도주스', '파인애플주스', '멜론주스']
item_name3 = ['초코 스무디', '딸기 스무디', '바닐라 스무디', '수박 스무디', '요거트 스무디']
item_name4 = ['바닐라 쉐이크', '초코 쉐이크', '그린티 쉐이크', '요거트 쉐이크', '딸기 쉐이크']
item_price = [2500, 3000, 4000, 4500, 5000, 5500, 6000]

def items_generator():
    items_data = {}
    items = []
    item_name = [item_name1, item_name2, item_name3, item_name4]
    
    # 타입별로 메뉴에 가격 붙이기
    for num in range(4): 
        
        for i in range(len(item_name[num])):
            item = {item_name[num][i] : random.choice(item_price)}
            items . append( item )
        items_data[item_type[num]] = items
        items = []

    return items_data
    
def print_items(select_print):
    items_data = [] # CSV 저장용 리스트
    
    list_data = list(data.keys())
    list_value = list(data.values())
    print('딕셔너리: ', list_value )
    for i in range(len(list_value)):
        print("대분류: ", list_data[i])
        for j in list_value[i]:
            for key, value in j.items():
                items_data .append ([ str(uuid.uuid4()), key, list_data[i], value ]) 
    
    print("아이템 샘플 데이터: ", items_data)
    
        
    if select_print == '1':
        with open('data_items.csv', 'w', encoding='utf-8') as file:
            writer = csv.writer(file)
            for i in items_data:
                writer.writerow(i)
    else:
        with open('data_items.csv', 'w', encoding='utf-8') as file:
            writer = csv.writer(file)
            for i in items_data:
                writer.writerow(i)
        for i_item in items_data:
            print(i_item)
            
my_choice = input("새로운 아이템 조합을 생성하시겠습니까? YES or NO: ")
if my_choice.upper() == 'YES':
    data = items_generator()
    
    select_print = input('[1] 아이템 조합 저장 or [2] 아이템 조합 저장&화면출력: [1] or [2] ')
    print_items(select_print)

