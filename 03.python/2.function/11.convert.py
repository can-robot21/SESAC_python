# 1. 문자를 입력받아 대소문자 변경


def convert_case(text):
    print(text)
    result = ""
    
    for i in text:
        
        if i.islower:
            result += i.upper()
        elif i.isupper:
            result += i.lower()
        else:
            result += i
        
    return result 

print(convert_case('Hello'))
print(convert_case('WelCOME'))
print(convert_case('GoodyBye'))
print(convert_case('Im Busy'))


# def convert_case2(text):
#     return ''.join([char.upper() if char.islower() else char in text for char.lower()])