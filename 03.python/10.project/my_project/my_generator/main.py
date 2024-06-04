# 01. 실행파일 인포트
# 02. 입력창 통해 실행
# 03 샘플데이터 분리

# import 실행파일
from components.generator_u import usersGenerate
from components.print import printUsers

while True:
    def main():

        # 인트로 입력창

        print('=========================================================')
        print('|                                                       |')
        print('|                  샘플 데이터 생성 V0.5                 |')
        print('|                                                       |')
        print('=========================================================')
        print('생성할 샘플 데이터를 선택하세요.')
        print('[U] 사용자 [S] 스토어 [I] 아이템 [O] 구매정보 [D] 구매상세')
        select_m = input('생성할 데이터를 선택해 주세요: ')  
        sort = ('U', 'S', 'I', 'O', 'D')    

        try:
            if select_m.upper() in sort:
                if select_m == "u":
                    num_users = input("생성할 사용자 데이터 수를 입력하세요: ")
                    data = usersGenerate(num_users)       
        except:
            print[' U / S / I / O / D  중에 입력해 주세요.']
            
        mode = int(input(' [1] CSV 파일생성 [2] CSV 생성 및 화면 출력: '))
        printUsers(select_m, mode, data)
        
            
    main()