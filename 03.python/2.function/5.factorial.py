def factorial(num):
    result = 1
    for i in range(num, 0, -1):
        result = result * i
    print(result)
            
factorial(5)
factorial(7)
factorial(3)