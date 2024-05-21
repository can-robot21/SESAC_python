numbers = [-3, -7, -2, -9, -1, -4, -5, -6, -8]

def find_max(numbers):
    max_num = numbers[0]
    print('가장 큰 수 출력하기: ')
    for i in numbers[1:]:
        if max_num < i:
            max_num= i
    print(f'가장 큰 숫자는 {max_num}입니다.')
    
            
    
find_max(numbers)