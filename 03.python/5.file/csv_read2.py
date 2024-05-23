import csv

file_path = 'mydata.csv'

with open(file_path, 'r', encoding='utf8') as file:
    csv_reader = csv.DictReader(file)
    
    for row in csv_reader:
        print(row["Name"]) # 딕셔너리 형식 데이터