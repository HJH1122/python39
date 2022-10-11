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








