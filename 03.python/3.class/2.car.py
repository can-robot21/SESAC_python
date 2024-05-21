class Car:
    make = ""
    model = ""
    ordometer = 0
    
    def get_name(self):
        print(f'{self.make} 의 {self.model}')
        
    def get_odometer(self):
        print(f'현재까지 주행거리는 {self.ordometer}입니다')
        
    def get_drive(self, mileage):
        # self.odometer = self.ordermeter + mileeage
        self.ordometer += mileage
        
    
mycar = Car()
mycar.make = '현대차'
mycar.model = '아이오닉'
    
mycar.get_name()
mycar.get_odometer()
mycar.get_drive(100)
mycar.get_name()
mycar.get_odometer()
mycar.get_drive(100)
mycar.get_odometer()
mycar.get_drive(100)
    
    
    