# 유저정보, 매장정보, 아이템(상품) 정보 CSV 에서 파일 읽어 생성
# CSV 데이터 읽어 db 구성 ( 유저정보 -> 매장정보 -> 아이템정보 -> id + 날짜 )
import csv
import uuid
import random

# data_stores.csv 읽고 선택된 입력된 숫자만큼 생성하기
def select_list(part, num_orders):
    list_full = []
    list_select = []
    
    if part == 1:
        i = 1 
    elif part == 2:
        i = 2
    elif part == 3:
        print_order()
    
        
        
    
    # 파일 읽어 저장하기
    with open('data_stores.csv', 'r', encoding='utf-8', newline='\n') as file:
        reader = csv.reader(file, delimiter=',')
        # 전체 매장 테스트 출력
        for row in reader:
            list_full.append(row)
    print("전체 리스트: ", list_full)
    
    
    # 지정된 숫자만큼 랜점 리스트 작성        
    for  i in range(num_orders):
        selected = random.choice(list_full)
        list_select.append(selected)
        print(f"{i+1} 번째 {selected}")
        
    print(f" 선택된 {num_orders} 개의 {part} 리스트: ")
    print('생성 완료')
        
def print_order():
    # 오더 리스트 저장하기
    print("저장하기 Ready")

part = int(input('랜덤 생성할 파트: (1.사용자/2.매장/3.조합해 생성하기)'))
num_orders = int(input('생성할 데이터수: '))
select_list(part, num_orders)