# 파일 입출력 할 때 사용하는 함수 ... open

# 파일
# charactier Meaning
# 'r' open for reading (default)
# 'w' open for writing, truncating the file first
# 'x' create a new file and open it for writing
# 'a' open for writing, appending to the end of the file if
# 'b' binary mode

# with open('example.txt', 'r') as file:
#     context = file.write("Hello, World")
    
# with open('example.txt', 'r') as file:
#     context = file.read()
#     print(context)
# print('텍스트 파일 쓰기를 완료했습니다.')

with open('example.txt', 'r') as file:
    for line in file:
        print(line, end='')
    