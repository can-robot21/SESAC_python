# 2. 문자열의 글자 수 세기
words = ['apple', 'banana', 'orange', 'dragonfruit']
words_lenght = [ len(number) for number in words ]
print('글자수: ',words_lenght)
# 출력: [5, 6, 6, 11]


# 4. 문자열의 리스트에서 길이가 3 이하인 단어들만 선택하기
words = ['apple', 'banana', 'cherry', 'dragonfruit', 'egg']
short_words = [ three for three in words  if len(three) <= 3]
print(short_words)
# 출력: ['egg']

# 5. 중첩 리스트 
nested_list = ([1, 2, 3], [4, 5, ], [6, 7, 8, 9])
# flattened_list = [num for number in nested_list for num in number]
flattened_list = [num[i] for num in nested_list for i in range(len(num))]

print(flattened_list)
# 출력: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 6. 특정 조건(5보다 큰것)을 만족하는 요소 필터링
numbers=[1, 2, 3, 4, 5, 6, 7 ,8, 9]
greater_than_five = [ number for number in numbers if number > 5]
print('6번: ', greater_than_five)
# 출력: [6, 7, 8, 9, 10]

# 7. 문자열 리스트에서 첫 글자가 모음인 단어들 선택하기
words = ['apple', 'banana', 'cherry', 'apricot', 'egg']

vowel_staring_words = [ x for x in words if x[0] in ['a', 'i', 'o', 'u', 'e']]
print(vowel_staring_words)
# 출력: ['apple', 'apricot', 'egg']