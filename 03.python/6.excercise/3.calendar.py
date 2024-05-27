import calendar

print('샘플================')
print(calendar.month(2024, 5))

print('만든달력============')
year = int(input("연도 입력(숫자): "))
input_month = int(input("월 입력(숫자): "))

# 달별로 출력할 일수 gkatn
months =[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = ['Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su']

# 전년도까지의 일수 before_day = ((year-1)*365) - (윤년회수)
before_year = 365 * (year-1)
before_yoon = int(year / 4) - int(year/100) + int(year/400)
print('전년도까지 일수: ', before_year)
print('전년도까지 윤년', before_yoon)
# 올해의 시작 요일 : 지난해 12월 31일 요일 다음 요일
# 올해는 윤년인가?

if year%4 == 0:
    if year % 100 != 0 or year % 400 == 0:
        months[1] = 29
        print('올해 2월은 윤달: ', months[1])

last_year = before_year + before_yoon # 지난해까지의 일수
last_month = 0 # 지난달까지의 일수

if input_month > 1:
    for i in range(input_month-1):
        last_month += months[i]
last_day = last_year % 7
last_day =  (last_year + last_month) % 7 # 지난달까지의 요일
print('입력된 달: ', input_month)
print('지난달까지의 날수: ', last_month)
print('지난달 마지막 주: ', last_day )

def print_month(year, input_month):
    this_month = []
    # 첫 주의 공백 추가해 출력할 이달의 리스트 완성
    for j in range(last_day):
        this_month.append('  ')

    print(this_month)    
    this_month += [num+1 for num in range(months[input_month-1])]
    
    print(f'        {input_month} {year}       ')
    for i in range(len(days)):
        print(days[i], end=" ")
    print("")
    
    
    for day in range(1, len(this_month)):
        if day % 7 != 0:
            print( f'{this_month[day]:>02} ',end="")
        else:
            print( f'{this_month[day]:>02} ',"")

print_month(year, input_month)