# print 함수

# 성적처리 프로그램 v1
# 이름, 국어, 영어, 수학을 이용해서
# 총점, 평균을 계산하고 출력함

name = '홍길동'
kor = 99
eng = 98
mat = 99

avg = (kor + eng + mat) / 3
total = kor + eng + mat

# 출력1
print(name)
print(kor, eng, mat)
print('총점', total)
print('평균', avg)

# 출력2
print('이름', name)
print('국어', kor,'영어', eng,'수학', mat)
print('총점', total)
print('평균', avg)

# 출력3 - 출력서식 사용 : % 문자 사용
# print(출력서식 % 변수들...)
# 출력서식 문자 : %d, %f, %s
print('이름 : %s' %name)
print('국어 : %03d, 영어 : %03d, 수학 : %03d' % (kor, eng, mat))
print('총점 : %d, 평균 : %.1f' % (total, avg))

# 출력4 - 인덱스, 출력서식 사용 : .format 함수 사용
# print({인덱스:출력서식}.format(변수들...))
print('이름 : {0:s}' .format(name))
print('국어 : {:03d}, 영어 : {:03d}, 수학 : {:03}' .format(kor, eng, mat))   # 인덱스 생략 가능
print('총점 : {0:d}, 평균 : {1:1f} ({1:f})' .format(total, avg))  # 특정변수를 반복출력 가능

print('총점 : {1:d}, 평균 : {0:1f} ({0:f})' .format(avg, total))  # 변수의 출력순서 재조정

# 출력5 - 문자열 템플릿(f-string) : py 3.6이후 지원 (추천!)
# print(f'{변수명:출력서식}')
print(f'이름 : {name:s}')
print(f'국어 : {kor:03d}, 영어 : {eng:03d}, 수학 : {mat:03d}')
print(f'총점 : {total:d}, 평균 : {avg:.1f} ({avg:f})')

# % 서식
print('7 x 1 = %d' % (7*1))
# .format
print('7 x 1 = {:d}'.format(7*1))

# f-stirng
print(f'7 x 1 = {7*1:2d}')

