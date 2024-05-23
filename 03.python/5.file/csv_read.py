import csv

file_path = 'mydata.csv'

with open(file_path, 'r', encoding='utf8') as file:
    csv_reader = csv.reader(file)
    print('읽은 원본: ', csv_reader)
    for row in csv_reader:
        print(row[0])  # 리스트 형식 데이터