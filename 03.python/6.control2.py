x = 10

if x < 10:
    print('x가 10보다 작습니다.')
else:
    print('x는 10보다 큽니다.')
    
score = 92

if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
    
print(score, grade)

print("Score: {}, Grade: {}".format(score, grade))

print("당신의 점수 {score} 는 {grade} 입니다.")     # 문자열
print(f"당신의 점수 {score} 는 {grade} 입니다.")    # 포맷팅

math = 85
eng = 80

if math >= 90 and eng >= 90:
    print('졸업조건 충족')
else:
    print('졸업조건 미흡')
    
if math >= 90 or eng >= 90:
    print('간신히 졸업!!')
else: 
    print('졸업 불가')

y = ''
for i in range(10):
    y += str(i) + ' '

print(y)