def hello():
    print('hello1')
    print('hello2')
    print('hello3')

hello()

def numbers(num1):
    result = num1 + 4
    return result
    
num1 = numbers(3)
num2 = numbers(4)

print(num1)
print(num2)

# -------------------------------------

# 미션1. 뎟셈을 하는 함수 작성
#     숫자 두개를 입력 받아서, 해당 숫자의 합을 반납

print('덧셈 :')
def add(num1, num2):
    return num1 + num2

print(add(10, 12))

def add3(num1, num2):
    return num1, num2, num1+num2

print(add3(2, 3))

# 미션2. 뺄셈, 곱셈, 나눗셈 함수 보기
#     모두 2개의 인자를 입력받아 하나의 결과를 반환하시오.

def minus(num1, num2):
    return num1+num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

print(minus(5, 2))
print(multiply(6, 2))
print(divide(8, 2))

    