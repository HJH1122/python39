#20





#22





#26 (0 : 미혼 , 1 : 기혼)
salary = int(input('연봉 입력:'))
isMarried = int(input('결혼 여부는? (0: 미혼, 1: 기혼)'))
tax = 0

if isMarried:
    if salary < 6000: tax = salary * 0.15
    else: tax = salary * 0.35
else:
    if salary < 3000: tax = salary * 0.1
    else: tax = salary * 0.25

print(salary, isMarried, tax)


#27
# 2020, 2008, 2000 윤년
# 2022, 1900, 2010 평년
year = int(input('연도는?'))

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(year, '는 윤년입니다')
else:
    print(year, '는 윤년이 아닙니다')




#25 - 복권 발행 프로그램














