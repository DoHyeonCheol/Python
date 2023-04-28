#리스트 [순서를 가지는 객체]

'''

#지하철 칸별로 10명, 20명, 30명

#기존방식
#subway1 = 10
#subway2 = 20
#subway3 = 30

subway = [10, 20, 30]   #비슷한 것을 하나의 리스트롤 묶음
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway)

# 조세호는 몇번칸에 타고 있을까?
print(subway.index("조세호"))    # index는 0 부터 시작함

# 하하가 다음 정류장에 다음칸에 탔을 때
subway.append("하하")
print(subway)

# 정형돈이 유재석과 조세호 사이에 탔을 때
subway.insert(1, "정형돈")   # 이름 보다 index를 먼저 입력해야 함
print(subway)

# 지하철에 있는 사람dl 한 명씩 뒤에서 내림
print(subway.pop())
print(subway)

# print(subway.pop())
# print(subway)
# print(subway.pop())
# print(subway)

subway.append("유재석")
print(subway)
print(subway.count("유재석"))   # 같은 값이 얼마나 나오는지 알 수 있는 것

'''

# 정렬

'''

num_list = [5, 2, 4, 3, 1]
num_list.sort()
print(num_list)

# 순서 뒤집기 가능
num_list.reverse()
print(num_list)

# 모두 지우기
num_list.clear()
print(num_list)

리스트는 자료형에 상관없이 함께 사용 가능
num_list = [5, 2, 4, 3, 1]
mix_list = ["유재석", 1, True]
# print(mix_list)

num_list.extend(mix_list)   # 리스트 2개 합치는 방법
print(num_list)

'''


# 사전 (Dictionary)

'''

cabinet = {1:"유재석", 2:"박명수", 3:"조세호", 100:"김태호"}   # 사전일때는 {}
print(cabinet[1])   # 1 번에는 유재석의 짐이 들어가있는 상태
print(cabinet[100])
print(cabinet.get(100))
# print(cabinet[5])  # 5라는 숫자는 없기에 오류가 나면서 종료가되고 Hi가 출력되지 않는 것
print(cabinet.get(5))# get을 사용하면 오류가 날때 종료가 아니라 None이라고 출력되고 다음 것들도 계속 진행되는 것
print(cabinet.get(5, "사용 가능"))   # None 말고 다른 글자를 출력하는 방법
print("Hi")

print(100 in cabinet)    # 100이라는 숫자가 cabinet에 있는지를 확인하는 것  (True or False)
print(5 in cabinet)

cabinet = {"A-1":"유재석", "A-2":"박명수", "A-3":"조세호", "A-100":"김태호"}
print(cabinet["A-1"])
print(cabinet["A-100"])

# 새 손님이 왔을 때
print(cabinet)
cabinet["A-4"] = "정형돈"
print(cabinet)
cabinet["A-2"] = "강호동"    # 기존의 A-2에 할당 되어 있는 것을 새로운 것으로 바꿀 수 있음  (박명수 -> 강호동)
print(cabinet)

# 손님이 갔을 때

del cabinet["A-100"]
print(cabinet)

# key들만 출력하는 방법
print(cabinet.keys())

# value들만 출력하는 방법
print(cabinet.values())

# key와 value 둘다 출력하는 방법
print(cabinet.items())

# 모든 데이터를 제거하는 방법
cabinet.clear()
print(cabinet)

'''



# 튜플 (속도가 list보다 빠르다는 장점)

'''

menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])
# menu.add("생선까스")    # 튜플은 값을 추가하거나 제거하는 것이 불가능하다는 것이 특징

# name = "김종국"
# age = 20
# hobby = "코딩"
# print(name, age, hobby)   # 기존방식

(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)   # 튜플이용방식

'''



# 집합 (set)  - 중복이 안되며, 순서가 없다는 것

'''

my_set = {1,2,3,3,3}   # 사전에서는 키와 값이 둘다 있어야하지만 set에서는 값만 있으면 된다는 것이 특징
print(my_set)   # 중복을 허용하지 않기에 {1, 2, 3}만 나옴

java = {"유재석", "김태호", "조세호"}
python = set(["유재석", "강호동"])

# 교집합 출력방법
print(java & python)  # 방법 1
print(java.intersection(python))  # 방법 2

# 합집합 출력방법
print(java | python)   # 방법 1
print(java.union(python))  # 방법 2

# 차집합 출력방법 (java만 할수 있는 사람)
print(java - python)   # 방법 1
print(java.difference(python))    # 방법 2

# python 할 줄 아는 사람이 늘어남
python.add("김태호")
print(python)

# 제거하는 방법
java.remove("김태호")
print(java)

'''


# 자료구조의 변경

'''

menu = {"커피", "우유", "주스"}
print(menu)
print(menu,type(menu))

menu = list(menu)
print(menu,type(menu))

menu = tuple(menu)
print(menu,type(menu))

menu = set(menu)
print(menu,type(menu))

'''


# 퀴즈

'''
당신의 학교에서는 파이썬 코딩 대회를 주최한다.
참석률을 높이기 위해 댓글 이벤트를 진행하기로 했다.
댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 된다.
추첨 프로그램을 작성하시오.

조건 1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20이라고 가정
조건 2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
조건 3 : random 모듈의 shuffle 과 sample을 활용

(출력 예제)
-- 당첨자 발표 --
치킨 당첨자 : 1
커피 당첨자 : [2, 3, 4]
-- 축하합니다 --

(활용 예제)
from random import *
list = [1,2,3,4,5]
print(list)
shuffle(list)
print(list)
print(sample(list, 1))
'''

from random import *
# users = [1,2,3,4,5,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
users = range(1, 21)   # 1부터 20까지 생성
users = list(users)   # 기존의 users는 range 타입이기에 리스트 형식으로 변환
shuffle(users)

winners = sample(users, 4)

print("-- 당첨자 발표 --")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))  #1 부터 끝까지 불러옴
print("-- 축하합니다 --")
