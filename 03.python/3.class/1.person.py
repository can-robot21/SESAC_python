class Person:
    # 명사, property 를 정의 할 수 있음
    name = ""
    age = 0
    
    def __init__(self, name, age):  # 이 객체의 초기화 함수
        self.name = name
        self.age = age
    
    # 메소드 
    def speak(self):
        print(f'[{self.name}]안녕하세요')
        
    def walk(self):
        print(f'[{self.name}]저는 걸어가는 중입니다')
        self.motion = 'walking'
        
    def running(self):
        print(f'[{self.name}]저는 뛰어가는 중입니다.')
        self.motion ='running'
        
    def introduce(self):
        print(f'안녕하세요. 저는 {self.name}이고 {self.age} 살 입니다')
        
    def motion(self):
        print(f'{self.name}: 나의 상태는 {self.motion} 입니다.')
        
# 사람(Person) 이라는 객체를 만들고
# 사람이 할 수 있는 행위(method) 인 speak 와 walk 를 정의
# 사람이라는 객체를 정의 (define) 한 상태
# 이 객체가 만들어지지 않은 상태
# 객체의 함수는 첫번째 인자가 self 여야 함.

# 이 객체를 통해서 사람을 만들기
alice = Person('Alice', 30)

# alice = Person()
# alice.name = 'Alice'
# alice.age = 30

alice.introduce()
alice.speak()
alice.walk()
alice.running()


# bob.name = 'Bob'
# bob.age = 26
bob = Person('bob', 26)
bob.introduce()
bob.speak()
bob.walk()