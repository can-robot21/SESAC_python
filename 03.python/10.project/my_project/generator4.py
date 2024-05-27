from generators.address_generator import AddressGenerator
from generators.birthdate_generator import BirthdateGenerator
from generators.gender_generator import GenderGenerator
from generators.id_generator import IdGenerator
from generators.name_generator import NameGenerator

import sys
        
class DataGenerator:
    number = 1
    data = []
    
    def __init__(self, num_users):
        self.number = num_users
        self.id_gen = IdGenerator()
        self.name_gen = NameGenerator()
        self.birthdate_gen = BirthdateGenerator()
        self.gender_gen = GenderGenerator()
        self.address_gen = AddressGenerator()
        self.data = []
        
    
    def generate_users(self):
        for _ in range(self.number):        
            id = self.id_gen.generate_id()
            name = self.name_gen.generate_name()
            birthdate = self.birthdate_gen.generate_birthdate()
            gender = self.gender_gen.generate_gender()
            address = self.address_gen.generate_address()        
        
            a_user = (id, name, birthdate, gender, address)
            self.data.append(a_user)

def print_to_screen(data):
    for d in users1.data:
        print(d)
        
def print_to_file():
    with open('output.txt', 'w') as file:
        for d in file:
            file.writer.writerow(d)
   
# 메인 함수     
if __name__ == "__main__":
    
    if len(sys.argv):
        num_data = input('생성을 원하는 데이터 개수를 입력하세요') 
    else: 
        num_data = sys.argv[1]   
    
    users1 = DataGenerator(20)
    users1.generate_users()
    
    # 화면 or 파일 출력부분
    print_to_screen(users1.data)
    print_to_file(users1.data)
