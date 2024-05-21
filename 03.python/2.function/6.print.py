#1. 일반 문자열 출력
print('hello')
print('hello world')
print('hello', 'world')

#2. f 문자열
print(f'hello {1}')
내변수 = '123'
print(f'hello {내변수}')
my_variable = '456'
print(f'hello {내변수}는 {my_variable}')

#3. 문자열 포맷팅 {} 사용
name = '홍길동'
print("Hello, {}".format(name))
print("Hello, {} 는 {} 입니다.".format(내변수, my_variable, name))

#4. 문자열 포맷팅에 순서 부여
print('-4-')
print("Hello")
print("Hello, {0} * {1} = {2}".format(내변수, my_variable, name))
print("Hello, {2} * {0} = {1}".format(내변수, my_variable, name))
print("Hello, {2} * {1} = {2}".format(내변수, my_variable, name))

#5. 문자열 연결 연산자
print('-5-')
print('hello', end="\n")
print('hello', end=" ")
print('sesac')

#6. % 연산자
print('-6-')
name = "John"  # 예시 이름
age = 25  # 예시 나이

print('-6-')
print('Hello, %s' % name)  # %s는 문자열
print('Hello, %d' % age)  # %d는 숫자
print('Hello, %s' % name)  # 변수를 전달
