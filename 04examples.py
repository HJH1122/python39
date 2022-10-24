#1
# 프로그래밍 언어 실습시 글꼴은
# 고정 폭 글꼴을 사용할 것을 추천
str1 = "☆     ☆            ☆☆          ☆☆☆☆           ☆☆☆☆         ☆    ☆            /////"
print(str1)

str2 = "☆     ☆          ☆    ☆        ☆     ☆         ☆     ☆       ☆     ☆          ㅣ o o ㅣ"
print(str2)

str3 = "☆☆☆☆☆         ☆      ☆       ☆☆☆☆           ☆☆☆☆           ☆ ☆           (ㅣ  ∧  ㅣ)"
print(str3)

str4 = "☆     ☆         ☆☆☆☆☆☆      ☆      ☆         ☆      ☆         ☆             ㅣ [_] ㅣ"
print(str4)


str5 = "☆     ☆         ☆      ☆       ☆        ☆       ☆        ☆      ☆               -----"
print(str5)

#2
소주 = 300 * 2
너나치킨 = 1200
총합 = 너나치킨 + 소주
과세합계 = round(총합 / 1.1)
부가세 = 총합 - 과세합계
받은금액 = 5000
잔액 = 받은금액 - 총합



print("소주"+str(소주)+"\n너나치킨"+str(너나치킨)+"\n과세합계"+str(과세합계)+"\n부가세"+str(부가세)+"\n총합"+str(총합)+"\n받은금액"+str(받은금액)+"\n잔액"+str(잔액))


#3
rate1 = 1
# 1stPlayer = 2        # 숫자로 시작해서 불가
# myprogram.java = 3   # . 때문에 불가
long = 4
TimeLimit = 5
numberOfWindow = 6


#4
x, y, z = 1, 2, 3
s0, v0, t, g = 4, 5, 6, 9.8

print(3 * x, 3 * x + y, (x + y) / 7)
print(s0 + v0*t + (1/2) * g * t**2)

l

#5
#가. double number = ( 1 / 3 ) * 3;          나. int quotient = 7 / 3;
#다. int remainder = 7 % 3;                  라. int result = 11; result /= 2;

#6
x, y, m, n = 2.5, 1.5, 18, 4

print(x + n * y - (x + n) * y)
print(m / n + m % n)
print(5 * x - n / 5)
print(1 - (1 - (1 -(1 - n))))

#7
print(3 + 4.5 * 2 + 27 / 8)
# 논리연산시 경우에 따라 단축식 평가가 적용되기도 함
print(True or False and 3 < 4 or not (5 == 7))
print(True or 3 < 5 and 6 >= 2)

#print(not True > 'A')
print(not True)
print(not True > bool('A'))  # not(True > True)


#print(7 % 4 + 3 - 2 / 6 * 'Z')
print(7 % 4 + 3 - 2 / 6 * bool('Z'))

#print('D' + 1 + 'M' % 2 / 3)
print(bool('D') + 1 + bool('M') % 2 / 3)
print( 1 + 1 % 2 / 3)

print((4 < 6) or True and False or False and (2 > 3))


#9
print(True and False and True or True)   #트루
print(True or True and True and False)   #트루
print((True and False)or(True and not False)or(False and not False))  #트루
print((2 < 3)or(5 > 2)and not(4 == 4)or(9 != 4))  #트루
print(6 == 9 or 5 < 6 and 8 < 4 or 4 > 3)  #트루

#10
print( 27 / 13 + 4)
print( 27 / 13 + 4.0)
print( 42.7 % 3 + 18)

# 논리식과 산술식(값)이 결합된 수식에서는
# 논리식의 결과가 True면 값이 출력
# 논리식의 결과가 False면 False가 출력
print((3 < 4) and 5 / 8)

print(23 / 5 + 23 / 5.0)
# print(2.0 + 'a')  # 문자와 정수/실수간 산술연산 불가
#print(2 + 'a')

print('a' + 'b')
#print('a' / 'b')  #문자간 산술연산 불가
print('a' and not 'b')
print('a' and 'b')
#print((float)'a' / 'b') # 문자는 실수로의 형변환 불가


#11
# K나이 - 세는나이(출생시 1살, 해가 바뀌면 + 1)
#        만나이(출생시 0살, 생일이 지나면 + 1)
#        연나이(현재연도 - 출생연도)

name = '홍길동'
weight = 55.5
age = 35

print(name, weight, age)



#12
# K나이 - 세는나이(출생시 1살, 해가 바뀌면 + 1)
#        만나이(출생시 0살, 생일이 지나면 + 1)
#        연나이(현재연도 - 출생연도)
birthYear = 1990
currentYear = 2022
isPassBirth = True


age = currentYear - birthYear
print('연나이', age)
print('세는나이', 1 + age)
# 파이썬 if 단축식 : 참일때 값 if 조건식 else 거짓일때 값
print('만나이', (age + 1) if isPassBirth else age)

#13
for x in range (2, 10):
    print("---------")
    for y in range (1, 10):
        print(x, "X", y, "=", x*y)





