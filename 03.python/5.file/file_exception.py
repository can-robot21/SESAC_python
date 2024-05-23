contents = "12345"

try:
    with open('file.txt', 'w') as file:
        # contents = file.read()
        file.write("Hello")

# except FileNotFoundError:
#     print("파일이 없습니다.")
except PermissionError:
    print("해당 파일에는 쓰기 권한이 없습니다.")
  
print("파일내용: ", contents)