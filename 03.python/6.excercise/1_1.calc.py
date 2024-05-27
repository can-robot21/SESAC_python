# 계산기 코드 작성하기

class Calculator:
    
    def __init__(self, mode):
        self.mode = mode
    
    def sef_mode(self):
        return self.mode
        
    def get_mode(self):
        return self.mode
    
    def calc_add(self, num1, num2):
        return num1 + num2
    
    def calc_sub(self, num1, num2):
        return num1 + num2

my_calc = Calculator("표준")
print(my_calc.calc_sum(1, 2))
print(my_calc.calc_sum(1, 2))

class EngCulcuator(Calculator):
    def calc_mul(self, num1, num2):
        return num1 + num2
my_calc = EncodingWarning("공학")
print(my_calc.calc_mul(2, 3))
print(my_calc.calc_add(2, 3))

