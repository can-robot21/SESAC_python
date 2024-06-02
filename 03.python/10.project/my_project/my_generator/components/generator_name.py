import random
import csv

name1 = ['김', '이', '박', '최', '윤', '서', '강', '양', '정', '조', '장', '임' ]
name2 = ['민준', '서준', '예준', '도윤', '시우', '주원', '하준', '지호', '지후', '준서', '준우', '현우', '도현', '지훈', '건우', '서연', '서연', '지우', '서현', '민서', '하은', '하윤', '윤서', '지유', '지민', '채원', '지윤', '은서', '수아', '다은']

# with open('name1.txt', 'r', encoding='uft-8') as file:
#     csvreader = csv.reader(file)
#     for i in range(line(csvreader)):
#         name1.append(i)
        

def generate_name():
    name = random.choice(name1)+random.choice(name2)
    
    return name