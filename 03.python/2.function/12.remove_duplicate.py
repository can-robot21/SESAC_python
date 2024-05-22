def remove_duplicate(lst):
    unique_lst = []
    lst.sort()
    num1 = lst[0]
    unique_lst.append(num1)
    
    for num in lst:
        if num1 != num:
            unique_lst.append(num)
            num1 = num
        
    return unique_lst

# 중복 미처리
def remove_duplicate2(numbers):
    unique_list = []
    
    for n in numbers:
        
        for u in unique_list:
            
            if n == u:
                print(n, u, '중복')
                break
            else:               
                print('중복아닌것')
                unique_list.append(n)
        
    return unique_list

# 조금더 파이썬 스러운 스타일
def remove_duplicate3(numbers):
    unique_list = []
    
    for n in numbers:
        if n in unique_list:
            pass
        else: 
            unique_list.append(n)
    return unique_list

# 모던 파이썬 스타일
def remove_duplicate4(numbers):
    return list(set(numbers))



numbers = [1,2,3,1,3,6,7,8,9,6,3]
unique_numbers = remove_duplicate(numbers)
unique_numbers2 = remove_duplicate2(numbers)
unique_numbers3 = remove_duplicate3(numbers)
unique_numbers4 = remove_duplicate4(numbers)


print('원본 리스트: ', numbers)
print('유닉 리스트: ', unique_numbers)
print('유닉 리스트2: ', unique_numbers2)
print('유닉 리스트3: ', unique_numbers3)
print('유닉 리스트3: ', unique_numbers3)
