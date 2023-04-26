# 연산자

# print(1+1)  #2
# print(100-53)  #47
# print(5*20)  #100
# print(100/5)  #20

# print(3**3)  #3^3=27
# print(100%12)  #100/12의 나머지 = 4
# print(100//12)  #100/12의 몫 = 8


# print(3 == 3)  #True
# print(3 + 11 == 15)  #False
# ==은 같다는 것을 표현함

# print(1 != 3) # True  # !는 같지 않다라는 것을 표현함
# print(not(1 != 3)) #Fasle
# print ((3 > 0) and (3 < 5 )) #True
# print ((3 > 0) & (3 < 5 ))  #True (and 하고 &은 같음)

# print((3 > 0) or (3 > 5)) #True
# print((3 > 0) | (3 > 5)) #True  (or 이랑 |는 같음 & 둘 중 하나만 true라도 true임)

# print(5 > 4 > 3)  # True
# print(5 > 4 > 7)  # False

# 간단한 수식

# print(2 + 3 * 4)  # 14
# print((2 + 3) * 4)  # 20

# num = 2 + 3 * 4  # 14
# print(num)
# num = num + 2 # 16
# print(num)
# num += 2  # 18 #num = num + 2와 같은 문구
# print(num)
# num *= 2 # 36
# print(num)
# num /= 2 # 18
# print(num)
# num %= 4   # 2
# print (num)


#숫자 처리 함수

# print(abs(-5))  # 5  abs는 절댓값을 의미
# print(pow(4, 2)) # 4^2는 16
# print(max(5, 12))  # max는 최댓값 찾기 12
# print(min(5, 12))  # min은 최솟값 5
# print(round(3.14))  # 3
# print(round(4.99))  # round는 반올림 하여 정수로만들기 5

# from math import *
# print(floor(4.99)) # floor은 내림 결과값 4
# print(ceil(3.14)) #  ceil은 올림 결과값 4
# print(sqrt(16))  #sqrt는 제곱근(루트) 결과값 4

#랜덤 함수

# from random import *

# print(random())  # 0.0 ~ 1.0 미만의 임의의 값을 생성하는 것
# print(random() * 10)  # 0.0 ~ 10.0 미만의 임의의 값을 생성하는 것
# print(int(random() * 10))  #0 ~ 10 미만의 임의의 값 생성
# print(int(random() * 10) +1)  #1 ~ 10이하의 임의의 값 생성

# #(로또번호 예제)
# print(int(random() * 45) + 1) # 1 ~ 45 이하의 임의의 값 생성
# print(int(random() * 45) + 1)
# print(int(random() * 45) + 1)
# print(int(random() * 45) + 1)
# print(int(random() * 45) + 1)
# print(int(random() * 45) + 1)

# print(randrange(1, 46))   # 1~ 45 미만의 임의의 값 생성 따라서 46으로 입력해야함
# print(randrange(1, 46))
# print(randrange(1, 46))
# print(randrange(1, 46))
# print(randrange(1, 46))
# print(randrange(1, 46))

# print(randint(1, 45))    # 1 ~ 45 이하의 임의의 값 생성


'''
#퀴즈

당신은 최근에 코딩 스터디 모임을 새로 만들었습니다.
월 4회 스터디를 하는데 3번은 온라인으로 하고 1번은 오프라인으로 하기로 했습니다.
아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성하시오.

조건1: 랜덤으로 날짜를 뽑아야 함
조건2 : 월별 날짜는 다름을 감안하여 최소 일수인 28일 이내로 정함
조건3: 매월 1~3일은 스터디 준비를 해야 하므로 제외

출력문 예제
오프라인 스터디 모임 날짜는 매월 X 일로 선정되었습니다.
'''

from random import *

#date = randrange(4, 29)
date = int(random() * 25 + 4)
#date = randint(4,28)
print("오프라인 스터디 모임 날짜는 매월 " + str(date) + "일로 선정되었습니다." )



