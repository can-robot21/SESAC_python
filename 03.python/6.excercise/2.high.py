# 게임 히스토리와 하이스코어 보여주기
total_list =[]

def input_score():
    # 스코어 입력하기
    # 이름입력하기
    print("점수/이름 입력 ======")
    while True:
        try:
            num = int(input("점수를 입력해 주세요: "))
            break
        except ValueError:
            print("점수는 숫자로 입력해 주세요.")
            
    user_name = input("이름을 입력해 주세요: ")    
    score = [num,user_name]
    total_list.append(score)
    
    return score

def high_score():
    # 하이스코어(순위) 보여주기
    print("현재 리스트: ", total_list)
    sorted_list = sorted(total_list, reverse=True)
    
    
    print("순위 =================")
    for i in range(len(sorted_list)):
        print(f' {i+1} 등: {sorted_list[i]}')
    
        
def list_score():   
    # 히스토리
    print("히스토리 =============")
    for i in range(len(total_list)):
        print(total_list[i])

while True:
    # 입력값으로 모드 정하기(스코어입력 / 하이스코어(순위) / 히스트로)
    select_mode = input("희망하는 모드(1.입력/2.순위/3.히스토리)를 선택하세요: ")
    print(select_mode)
    
    if select_mode == '1':
        input_score()
        
    if select_mode == '2':
        high_score()
        
    if select_mode == '3':
        list_score()        