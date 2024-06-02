# [파일저장]이나 [파일저장 & 화면출력] 선택 처리   
import csv

def printData(sorted, data):
    sort = ('u', 's', 'i', 'o', 'd')     
    csvFile = ""
    
    if  sorted == 'u':
        csvFile = 'data_users.csv'
    elif sorted == "s":
        csvFile = 'data_stores.csv'
    elif sorted == 'i':
        csvFlle = 'data_orders.csv'
    elif sorted == 'o':
        csvFile = 'data_orders.csv'
    elif sorted == 'd':
        csvFile = 'data_orderItems.csv'   
        
    mode = input("출력방식 선택 [1] CSV 파일만 생성, [2] CSV 생성 후 화면출력: ")    
                
    if mode == "1":
        # 유저파일 CSV 저장
        with open('../file/'+csvFile, 'w', encoding='utf-8') as file:
            writer = csv.writer(file)
            for u in data:
                writer.writerow(u)
    elif mode == "2":
        # 유저 파일 CSV저장 및 화면 출력
        with open('data_stores.csv', 'w', encoding='utf-8') as file:
            writer = csv.writer(file)
            for u in data:
                writer.writerow(u)
        print('파일저장 완료 저장 데이터 출력: ', data)
        for i in data:
            print(str(i))
            
    else:
        print('데이터 처리는 [1] 과 [2] 중 선택해 주세요.')
        