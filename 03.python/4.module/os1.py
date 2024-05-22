import os

current_dir = os.getcwd()
print('현재 작업 디렉토리는: ',current_dir)


# 디렉토리 생성
new_dir = "myFolder1234"
os.mkdir(new_dir)

# 디렉토리 삭제
os.rmdir(new_dir)
print('디렉토리 생성')

my_path = os.getenv("PATH")
print('나의 환경변수', my_path)

command = 'dir'
os.system(command)

os.chdir("C:/project/sesac/SESAC_python")
print(f"현재 폴더: {os.getcwd()}")
os.system(command)