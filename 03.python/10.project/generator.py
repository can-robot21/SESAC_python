import random

surnames = ['박', '이', '김', '최', '서', '윤']
middlenames = ['수', '태', '미', '여' '윤', '진']
lastnames = ['현', '서', '원', '진', ]

def generator_name():
    return random.choice(surnames)+random.choice(middlenames)+random.choice(lastnames)

for _ in range(10):
    print(generator_name())