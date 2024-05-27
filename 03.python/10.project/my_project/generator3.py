import random
import uuid
import csv
from itertools import chain

class IdGenerator:
    def generate_id(self):        
        return str(uuid.uuid4())

class NameGenerator: 
    names = []
    
    def __init__(self):
                
        with open('names.txt', 'r') as file:
            # names = file.read().splitlines()
            csvreader = csv.reader(file)
            csv_list_names = [n for n in csvreader]
            names_list = list(chain(*csv_list_names))
            self.names = [n.strip() for n in names_list]
        
    def generate_name(self):
        return random.choice(self.names)
    
class AddressGenerator:
    cities = []
    
    def __init__(self):    
        with open('cities.txt', 'r') as file:
            csvreader = csv.reader(file)
            csv_list_cities = [line for line in csvreader]
            data = list(chain.from_iterable(csv_list_cities))
            self.cities = [n.strip() for n in data]     
        
    def generate_address(self):
        city = random.choice(self.cities)
        street = random.randint(1, 100)
        return f"{street} {city}"


class BirthdateGenerator:
    year_start = 1980
    year_end = 2005
    
    def generate_birthdate(self):
        year = random.randint(self.year_start, self.year_end)
        month = random.randint(1, 12)
        day = random.randint(1, 28)
        return f"{year}-{month:02d}-{day:02d}"

class GenderGenerator:
    gender = ['Male', 'female']
         
    def generate_gender(self):
        return random.choice(['Male','Female'])
        
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
    
    def generate_users(self):
        self.data = []
        for _ in range(self.number):        
            id = self.id_gen.generate_id()
            name = self.name_gen.generate_name()
            birthdate = self.birthdate_gen.generate_birthdate()
            gender = self.gender_gen.generate_gender()
            address = self.address_gen.generate_address() 
            
            self.data.append((id, name, birthdate, gender, address))       
        
            # a_user = (id, name, birthdate, gender, address)
            # data.append(a_user)
   
# 메인 함수     
if __name__ == "__main__":
    
    users1 = DataGenerator(20)
    users1.generate_users()
    
    for d in users1.data:
        print(d)
        
