#  리스트 (list)
a = 5
a2 = [5]
b = [1, 2, 3, 4, 5]

print(a)
print(b)

print(b[0])
print(b[4])
# print(b[5])

print(len(b))   # 리스트의 길이
                # 인텍스는 0부터
print(b[1:3])   # 리스트의 앞은 포함, 뒤는 미포함

fruits = ['apple', '사과', 'grape', '포도']
print(fruits)
print(fruits[1:4])

members1 = [3, 'desk', 2, -1, 'chair']
print(members1)

b.remove(2)
print(b)

fruits.remove('apple')
print(fruits)

# insert 삽입, append 덧붙이기 ..
b.append(20)
print(b)

b.insert(1,30)
print(b)

a2.insert(0, 10)
print(a2)

# ---------------------------------------
# 3.튜플 (Tuple) - 리스트와 동일한데, 변경 불가한 리스트를 강조

c = (1, 2, 3, 4, 5)

# c.remove(2)
# c.append(3)

print(c[3], c[4])
print(c[2:])
print(c[:2])
print(b[:2])

# -----------------------------------------
# 4. 딕셔너리

user1 = {
    "name": "park",
    "age": 10,
    "city": "seoul"
}

print(user1)
print(user1['name'])
print(user1['age'])
print(user1['city'])
      
user1['email'] = 'mantongnet@gmail.com'
print(user1)

user1['email'] = ''
print(user1)