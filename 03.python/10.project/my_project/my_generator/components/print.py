# [파일저장]이나 [파일저장 & 화면출력] 선택 처리   
from print import printUsers

def printUsers(mode, data):
    if mode == "1":
        # 유저파일 저장
        with open('data_users.csv', 'w', encoding='utf-8') as file:
            writer = csv.writer(file)
            for u in data:
                writer.writerow(u)
        print('파일생성 완료')
    elif mode == "2":
        # 유저 파일저장 및 화면 출력
        with open('data_stores.csv', 'w', encoding='utf-8') as file:
            writer = csv.writer(file)
            for u in data:
                writer.writerow(u)
        print('파일저장 완료 저장 데이터 출력: ', data)
        for i in data:
            print(str(i))
    else:
        print('데이터 처리는 [1] 과 [2] 중 선택해 주세요.')