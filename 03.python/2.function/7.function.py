def print_gugudan(dan=2, max=9):
    print(f'{dan} 단 ======')
    for i in range(1, max+1):
        print(f'{dan} * {i} = {max*i}')
    
print_gugudan(3, 9)