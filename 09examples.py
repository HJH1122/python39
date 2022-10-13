#20





#22 - if문의 함정
number = 30

if ( number % 2 == 0 ): print('입력한 값은 짝수입니다')
print('입력한 값은 홀수입니다') # 이부분은 if문에 상관없이 무조건 출력

if ( number % 2 == 0 ): print('입력한 값은 짝수입니다')
else: print('입력한 값은 홀수입니다')




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




#25 - 복권 발행 프로그램 v1
#난수 생성시 random 모듈의 randrange(st, ed-1)
import random as rnd
yourkey = int(input('복권 번호는?'))
lottokey = rnd.randrange(111, 1000)
print(lottokey)

if yourkey == lottokey:
    print('복권 당첨!! - 상금 백만원!!')
else:
    print('꽝 다음 기회에!!')












