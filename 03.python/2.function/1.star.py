row = input('출력을 원하는 별 수 :', )
num_row = int(row)
for i in range(1,num_row+1):
    print('*' * i)

# row = input('출력을 원하는 별 수 :', )
# for i in range(1,int(row)+1):
#     print('*' * i)

# 입력받은 숫자의 역순 * 출력
rows = input('출력을 위하는 별 수 : ')
num_rows = int(rows)
for i in range(1, num_rows+1):
    j = num_rows - i
    k = i
    print(" "*j,'*'*k)

# * 트리 만들기
rows = int(input('원하는 별의 숫자: '))
for i in range(1, rows):
    print(' '*(rows-i),'*'*(2*i-1))

# 마름모 만들기(?)

for i in range(1, rows):
    print(' '*(i-1), '*'*(rows-i))