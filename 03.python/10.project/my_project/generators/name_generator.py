import csv
import random
from itertools import chain

class NameGenerator: 
    names = []
    
    def __init__(self):        
        with open('names.txt', 'r') as file:
            reader = csv.reader(file)
            data = [n for n in reader]
            data = list(chain(*data))
            self.names = [n.strip() for n in data]
        
    def generate_name(self):
        return random.choice(self.names)