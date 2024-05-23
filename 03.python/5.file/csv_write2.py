import csv

file_path = 'mydata2.csv'

data = [
    # ['Name', 'Age', 'City'],
    # ['John', '20', 'Seoul'],
    # ['Jane', '25', 'Busan'],
    # ['Bob', '30', 'Jeju']
    {'Name':'김혜수', 'Age':'20', 'City':'Seoul'},
    {'Name':'마동석', 'Age':'25', 'City':'Busan'},
    {'Name':'고윤정', 'Age':'30', 'City':'Jeju'},
]

with open(file_path, 'w', encoding='utf-8', newline="") as file:
    headers = ["Name", "Age", "City"]
    
    csv_writer = csv.DictWriter(file, fieldnames = headers)
    
    # 헤더 쓰기
    csv_writer.writeheader()
    csv_writer.writerows(data)
    
print('CSV 파일 작성 완료')