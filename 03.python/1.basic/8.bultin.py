while True:
    # a = input('숫자를 입력하세요 : ')
    # print(a)
    
    # 미션3. 숫자를 두개 입력 받아서 덧셈 결과를 출력하시오.
    
    def add(num1, num2):
        a = int(num1)
        b = int(num2)
        return a+b
    
    a = input('숫자1을 입력하세요 :')
    b = input('숫ㅈ2를 입력하세요 :')
    
    sum = add(a, b)
    print(f' 두 숫자의 합은 {sum} 입니다.')