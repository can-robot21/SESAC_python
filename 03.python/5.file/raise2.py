class CustomError(Exception):
    # 속성
    # Mathod
    def __init__(self, message):
        self.message = message
        
    def __str__(self):
        return f'CustomError: {self.message}'

def check_value(value):
    if value < 0 or value > 100:
        raise CustomError("입력값은 0보다 작거나 100보다 클 수 없습니다.")
    return value

result = check_value(50)
result = check_value(20)

try:
    result = check_value(100)
except CustomError as e:
    print(e)
    
print(result)