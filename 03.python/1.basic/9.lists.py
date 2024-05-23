# list comprehension 리스트 컴프리헨션
# []
# [표현식 for 항목 in 반복 {조건문}]

# 1. 1부터 10까지의 숫자를 담는 리스트를 생성하시오. 
nums = [num for num in range(1, 10)]
        # 최종표현할 변수명(num) for 항목(num) in 반복(range(1, 10))
        
print(nums)

# 2. 위 리스트의 각 숫자의 제곱을 구하고 싶으면?
# [1, 2, 3, ...9]
# [1, 4, 9, ...81]
squares = [ x ** 2 for x in range(1, 10)]
print(squares)

# 3. 1 부터 20 까지의 짝수들로 이루어진 리스트 
even_numbers = [x for x in range(1, 20+1) if x % 2 == 0 ]
print(even_numbers)

odd_numbers = [x for x in range(1, 20+1) if x % 2 == 1]
print(odd_numbers)

# 4. 문자열의 각 글자를 대문자로 바꾼 리스트를 새성하시오. 
word = 'hello'
upper_letters = [x.upper() for x in word]
print(upper_letters)
upper_letters = ''.join([x.upper() for x in word])
print(upper_letters)