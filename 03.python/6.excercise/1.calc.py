# 계산기 코드 작성하기
# 1. 연산자(사칙연산) 및 두개의 숫자를 입력받아 그 결과를 출력하시오. 
# 2. 무한반복하기

def add(num1, num2):
    result = num1 + num2
    return result

def minus(num1, num2):
    result = num1 - num2
    return result

def multiply(num1, num2):
    result = num1 * num2
    return result

def divide(num1, num2):
    if num1 == 0 or num2 == 0:
        print(" 0 으로는 나눌 수 없습니다. ")
    else:
        result = num1 / num2
    return result

print("사칙연산 계산기 ***")

while True:
     
    tool = ['+', '-', '*', '/', 'stop']
    
    # 연산자 체크 + 정수체크

    calculate = input("원하는 연산 '+'  |  '-' | '*' | '/' 중 하나를 입력해 주세요.")
    try:
        if calculate in tool:            
            num1 = input("첫번째 숫자를 입력하세요: ")
            num2 = input("두번째 숫자를 입력하세요: ")   
        elif calculate == 'stop':
            break
        else:
            print("연산자는 +, -, *, / 이외에 stop 만 가능합니다. 연산자를 다시 입력해 주세요")

        input_num1 = int(num1)
        input_num2 = int(num2)            
        
        if calculate == '+':
            result = add(input_num1, input_num2)
            print("덧셈 결과는: ", result)

        elif calculate == '-':
            result = minus(input_num1, input_num2)
            print('뺄셈 결과는: ', result)

        elif calculate == '*':
            result = multiply(input_num1, input_num2)
            print('곱셈 결과는: ', result)

        elif calculate == "/":
            result = divide(input_num1, input_num2)
            print("나눗셈 결과는: ", result)

        else:
            print("연산자를 제대로 다시 입력하세요.")
    except ValueError:
        print('입력값이 숫자가 아닙니다. 숫자를 입력해 주세요.')

    

    