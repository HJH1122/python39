# p78  ex2) 숫자 맞추기(1~10)
import random

print('숫자맞추기 게임')
com = random.randint(1, 10)  # 난수 초기화

while True:
    my = int(input('예상 숫자 입력:'))
    if my == com:
        print('맞추셨습니다')
        break
    elif my > com:
        print('컴퓨터보다 큰수를 입력했습니다')
    elif my < com:
        print('컴퓨터보다 작은수를 입력했습니다')

#  ex30) 숫자 맞추기(1~100)
import  random

num2 = random.randint(1, 100)

while True:
    num1 = int(input('1~100 사이 임의의 숫자 입력:'))
    if num1 > num2:
        print('추측한 숫자가 큽니다')
    elif num1 < num2:
        print('추측한 숫자가 작습니다')
    else:
        print('정답')
        break


# ex25) 복권 프로그램 - 3자리수 난수 생성/입력
# 난수 범위 - 100~999, 위치는 상관없이 숫자만 일치여부 판단
# ex) 123 -> 345(1), 317(2), 312(3)
# 문자열 슬라이싱을 위한 문자열 변환 함수 -> str 함수 사용
# 3개 일치 - 상금 백만원
# 2개 일치 - 상금 5만원
# 1개 일치 - 상금 1천원
# 0개 일치 - 꽝

import random as rnd

lotto = str(rnd.randint(100, 999))
#lotto1 = str(rnd.randint(1, 9))
#lotto2 = str(rnd.randint(1, 9))
#lotto3 = str(rnd.randint(1, 9))
#lotto = lotto1 + lotto2 + lotto3


mykey = str(input('3자리 복권 번호는? (100~999)'))
match = 0  #일치여부 저장

# 첫째 자리 비교
#if lotto[0] == mykey[0] or lotto[0] == mykey[1] or lotto[0] == mykey[2]:
#    match += 1
# 둘째 자리 비교
#if lotto[1] == mykey[0] or lotto[1] == mykey[1] or lotto[1] == mykey[2]:
#    match += 1
# 셋째 자리 비교
#if lotto[2] == mykey[0] or lotto[2] == mykey[1] or lotto[2] == mykey[2]:
#    match += 1


# 개선된 코드1
#for i in range(3):
#    if lotto[i] == mykey[0] or lotto[i] == mykey[1] or lotto[i] == mykey[2]:
#        match += 1

# 개선된 코드1b
for i in range(3):
    if lotto[i] == mykey[0]: match += 1
    if lotto[i] == mykey[1]: match += 1
    if lotto[i] == mykey[2]: match += 1

# 개선된 코드 2
for i in range(3):
    for j in range(3):
        if lotto[i] == mykey[j]: match += 1


# 당첨여부 판단
if match == 3: print('당첨! 상금 백만원')
if match == 2: print('당첨! 상금 만원')
if match == 1: print('당첨! 상금 천원')
if match == 0: print('꽝')

#결과출력
print(lotto, mykey, match)