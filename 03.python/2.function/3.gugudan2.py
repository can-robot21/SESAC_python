dan = int(input('입력받은 숫자의 구구단: '))

def print_gugudan(num):
    print(f'{num} 단 ======')
    for i in range(1, 10):
        print(f'{num} * {i} = {num*i}')
    
print_gugudan(dan)

def print_gugu():
    for j in range(2,10):
        print_gugudan(j)
        
print_gugu()