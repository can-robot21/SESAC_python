import csv

file_path = 'mydata.csv'

data = [
    ['Name', 'Age', 'City'],
    ['John', '20', 'Seoul'],
    ['Jane', '25', 'Busan'],
    ['Bob', '30', 'Jeju']
]

with open(file_path, 'w', encoding='utf8', newline="") as file:
    csv_writer = csv.writer(file)
    # csv_writer.writerow(['이름', '나이'])
    # csv_writer.writerow(['길동', 30])
    # csv_writer.writerow(['영희', 2])
    # for d in data:
    #     csv_writer.writerow(d)
    csv_writer.writerows(data)
    
print('CSV 파일 작성 완료')