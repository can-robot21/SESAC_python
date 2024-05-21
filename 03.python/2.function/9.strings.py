s = 'Hello World'
l = 'hellow'
u = 'HELLO'
print(s)


print(type(s))
print(s.lower())
print(s.upper())
print(s.islower())
print(s.isupper())
print(l.islower())
print(l.isupper())
print(l.capitalize())
print(l.title())

s2 = ' hello world  !! '
print(s2.strip())  # <-- 앞뒤의 공백만 제거
s3 = 'apple, banana, cherry, orange'
print(s3.split())
print(s3.split(','))

s3_list = s3.split(',')
print(s3_list)

s3_clean_list =  []
for fruit in s3_list:
    clean_name = fruit.strip()
    s3_clean_list.append(clean_name)
    
print(s3_clean_list)

# ---------------------------------

def parse_input(input):
    s3_clean_list =  []
    for fruit in s3_list:
        clean_name = fruit.strip()
        s3_clean_list.append(clean_name)
        
        return s3_clean_list
    
s4_list = parse_input(s3)

# list_comprehension (리스트 컴프리헨션) = 파이썬 특징