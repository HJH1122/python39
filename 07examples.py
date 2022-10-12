# ex) 주민번호에서 생년과 월, 일, 성별을 추출해서
# 각 변수에 적절히 저장하세요
jumin = '202205092123456'

year = jumin[0:4]
month = jumin[4:6]
day = jumin[6:8]
gender = jumin[8]


# 14 - 시간 계산
time = 1234567890
days = time // 86400    # 정수부만 추출

time = 98765
hours = time // 3600

time = 12345
mins = time // 60




# 16 - 잔돈 계산
#비용과 지불금액을 입력받아 잔돈 계산

#지불금액은 ?원 이고,
#받은금액은 ?원 이고,
#잔액은 ?원 입니다

#50000원권은 ?장, 10000원권은 ?장,
#5000원권은 ?장, 1000원권은 ?장,
#500원은 ?개, 100원은 ?개,
#50원은 ?개, 10원은 ?개 입니다


cost = 12340
money = 50000
charge = money - cost     # 37660

# 50000원권 계산
w50k = int(charge / 50000)  #0
charge = charge - (w50k * 50000)

# 10000원권 계산
w10k = int(charge / 10000)  #3
charge = charge - (w10k * 10000)

# 5000원권 계산
w5k = int(charge / 5000)    #1
charge = charge - (w5k * 5000)

# 1000원권 계산
w1k = int(charge / 1000)    #2
charge = charge - (w1k * 1000)

# 500원권 계산
w5m = int(charge / 500)    #1
charge = charge - (w5m * 500)

# 100원권 계산
w1m = int(charge / 100)    #1
charge = charge - (w1m * 100)

# 50원권 계산
w50 = int(charge / 50)    #1
charge = charge - (w50 * 50)

# 10원권 계산
w10 = int(charge / 10)    #1
charge = charge - (w10 * 10)

# 결과 출력
print(w50k, w10k, w5k, w1k, w5m, w1m, w50, w10)


# 파이썬에서 제공하는 몫/나머지 연산자를 이용하면
# 수식이 좀 더 간단해짐

cost = int(input('비용은?'))
money = int(input('지불금액은?'))
charge = money - cost

# 50000원권 계산
w50k = charge // 50000
charge = charge % 50000

# 10000원권 계산
w10k = charge // 10000
charge = charge % 10000

# 5000원권 계산
w5k = charge // 5000
charge = charge %5000

# 1000원권 계산
w1k = charge / 1000
charge = charge %1000

# 500원권 계산
w5m = charge // 500
charge = charge %500

# 100원권 계산
w1m = charge // 100
charge = charge %100

# 50원권 계산
w50 = charge // 50
charge = charge %50

# 10원권 계산
w10 = charge // 10
charge = charge %10

# 결과 출력

print(f'''
50000원권은 {w50k}장, 10000원권은 {w10k}장,
5000원권은 {w5k}장, 1000원권은 {w1k}장,
500원은 {w5m}개, 100원은 {w1m}개,
50원은 {w50}개, 10원은 {w10}개 입니다
''')

