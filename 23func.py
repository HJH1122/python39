# 함수function
# 주어진 입력값으로 무언가를 수행하고 결과물을 내놓는 객체
# 한번 작성해두면 언제든 재사용 가능
# 논리적인 단위 분할 가능 -> 개발의 분업화
# 코드의 구현을 외부로 부터 숨길수 있음 -> 캡슐화

# 함수 정의
# def 함수이름(매개변수):
#     함수몸체

# 함수 호출
# 함수이름(인수)

# 인사말 출력하는 코드 1
print('Hello, World!!')


# 인사말 출력하는 코드 2 - 3번 반복
#print('Hello, World!!')
#print('Hello, World!!')
#print('Hello, World!!')
for _ in range(3):
    print('Hello, World!!')


# 인사말 출력하는 코드 3 - 3번 반복하는 코드를 3번 반복한다면?
# 복붙으로 해결할 수 있지만 수정사항이 생기면 유지보수가 힘듬
for _ in range(3):
    print('Hello, World!!')
for _ in range(3):
    print('Hello, World!!')
for _ in range(3):
    print('Hello, World!!')


# 인사말 출력하는 코드 4 - 함수
def sayHello():         # 함수 정의
    for _ in range(3):
        print('Hello, World!!')

sayHello()              # 함수 호출
sayHello()
sayHello()


# 매개변수parameter vs 인수argument
# 매개변수 : 함수 정의시 입력으로 전달된 값을 받는 변수
# 인수 : 함수 호출시 실제 입력으로 전달하는 값

def sayHello(msg):
    for _ in range(3):
        print(f'Hello, {msg}!!')

sayHello('python')
# python : 함수호출시 함수내부로 전달하는 실제값

sayHello('Java')

# ex) 두수를 입력받아 add라는 함수로 호출해서 결과 출력
# 단, add라는 함수는 두 입력값을 더한 후 결과 출력

def addNums():
    a = int(input('첫번째 숫자는?'))
    b = int(input('두번째 숫자는?'))
    print(f'{a}+{b}={a+b}')

addNums()


def addNums(a, b):
    print(f'{a}+{b}={a+b}')

a = int(input('첫번째 숫자는?'))
b = int(input('두번째 숫자는?'))
addNums(a, b)

# 함수 다중정의 - overloading
# 동일한 이름의 함수를 매개변수에 따라 다른 기능으로
# 동작하도록 작성하는 것을 의미
# 파이썬에서는 공식적으로 지원하는 기능은 아님 - 구현은 가능
# 다중정의를 너무 남발하면 코드가 복잡해짐


# ex) 잔돈계산하는 프로그램을 함수로 작성
# 함수명 : computeCharge(비용, 지불)


def computeCharge(cost, money):
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
    w1k = charge // 1000
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

    print(f'비용은 {cost:,d}이고, 받은금액은 {money:,d} 이며, 잔액은 {money - cost:,d} 입니다')

    print(f'''
    50000원권은 {w50k}장, 10000원권은 {w10k}장,
    5000원권은 {w5k}장, 1000원권은 {w1k}장,
    500원은 {w5m}개, 100원은 {w1m}개,
    50원은 {w50}개, 10원은 {w10}개 입니다
    ''')


cost = int(input('비용은?'))
money = int(input('지불금액은?'))

computeCharge(cost, money)



# ex) 신용카드 판별하는 프로그램을 함수로 작성
# 함수명 checkCredit(코드)
# dict 자료구조를 이용해서 작성

def checkCredit(code):
    cards = { '356317':'농협jcb카드' , '356901':'비씨비자카드', '356912': '국민 jcb카드', '404825':'비씨 비자카드'
              ,'438676':'신한비자카드', '457973':'국민 비자카드', '515694':'신한마스터카드', '524353':'외환 마스터카드'}

    cardname = cards.get(code)
    if cardname == None: print('카드번호가 잘못되었습니다')
    else: print(cardname)

code = input('조회할 카드번호는?')
checkCredit(code)




# ex) 60갑자를 출력해주는 프로그램을 함수로 작성
# 함수명 : checkChinaZodiac(년도)

def checkChinaZodiac(year):
    baseYear = 1444
    ten = ('갑', '을', '병', '정', '무', '기', '경', '신', '임', '계')
    twelve = ('자', '축', '인', '묘', '진', '사', '오', '미', '신', '유', '술', '해')
    animal = ('쥐', '소', '호랑이', '토끼', '용', '뱀', '말', '양', '원숭이', '닭', '개', '돼지')

    t10idx = (year - baseYear) % 10
    t12idx = (year - baseYear) % 12
    print(f'{year}년은 {ten[t10idx]}{twelve[t12idx]}년'f'({animal[t12idx]}의 해) 입니다')

year = int(input('년도?'))
checkChinaZodiac(year)



