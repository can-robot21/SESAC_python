# 01. 실행파일 인포트
# 02. 입력창 통해 실행
# 03 샘플데이터 분리

# import 실행파일
from components.generator_u import usersGenerate, printUsers
from components.print import printUsers

def main():

    # 인트로 입력창

    print('=========================================================')
    print('|                                                       |')
    print('|                  샘플 데이터 생성 V0.5                 |')
    print('|                                                       |')
    print('=========================================================')
    print('생성할 샘플 데이터를 선택하세요.')
    print('[1] 사용자 [2] 스토어 [3] 아이템 [4] 구매정보 [5] 구매상세')
    select_m = int(input('생성할 데이터를 숫자로 입력하세요: '))            

    try:
        if select_m in range(1, 6):
            if select_m == 1:
                num_users = int(input("생성할 사용자 데이터수를 입력하세요: "))
                data = usersGenerate(num_users)
                
        mode = int(input(' [1] CSV 파일생성 [2] CSV 생성 및 화면 출력: '))
        printUsers()
    except:
        print['1~5 중에 입력해 주세요.']