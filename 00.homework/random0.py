import random

# 5. 랜덤으로 문자열 생성(영문 대문자 6자리)
num = 6
word = 'ABCDEFGHIJKLMNOPQRSTUVXZ'

def random_text(num):
    result = ""
    i = 0
    
    while i < num:
        number = random.randint(1, len(word)-1)
        result+=word[number]
        i += 1
    return result

words = random_text(num)
print(words)

# 6. 랜덤 초이스에서 가중치를 고려한 랜덤

my_word = [word[num] for num in range(len(word))]
my_weight = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 3]
my_text =random.choices(my_word, k=6, weights=my_weight)
    
print("랜덤 초이스 가중치 적용: ", my_text)

# 7. 랜덤 비밀번호 생성(대소문자, 숫자포함 8자리)

number = "123456790"
low_word = word.lower()
my_word2=word+number+low_word

my_text2 = (random.choices(my_word2, k=8))
print("8자리 랜덤 비밀번호: ", my_text2)


# 8. 강력한 비밀번호 생성(대문자, 소문자, 숫자를 각각 최소 1개이상 포함하는 8자리를 만들려면??)
key = 8
a=random.randint(1, 8)
b=random.randint(1, 7)
c=a+b
d=random.randint(1, 6)
print(a, b, c)