list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

zipped = zip(list1, list2)
print(list(zipped))

list3 = [True, False, True]
zipped = zip(list1, list2, list3)
print(list(zipped))

# zip 으로 묶을때는 가장 짧은 데이터를 기준으로 묶임


keys = ['name', 'age', 'phone']
values = ['Alice', 25, '010-123-4567']
my_dicts = dict(zip(keys, values))
print(my_dicts)

values_list = [
    ['Alice', 25, '010-123-4567'],
    ['Tom', 22, '010-123-1111'],
    ['Jane', 18, '010-123-0000'],
]

# 딕셔너리 만들기