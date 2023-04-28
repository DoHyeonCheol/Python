# if문

'''

# weather = input("오늘 날씨는 어때요?")
# if weather == "비" or weather == "눈":
#     print("우산을 챙기세요.")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요.")
# else :
#     print("준비물 필요 없어요.")

temp = int(input("기온은 어때요?"))
if temp >= 30:
    print("너무 더우니 나가지 마세요.")
elif 10 <= temp and temp < 30:
    print("야외활동하기 좋은 날씨에요")
elif 0 <= temp < 10:
    print("쌀쌀한 날씨니 외투를 챙기세요")
else:
    print("밖이 추우니 나가는걸 자제하세요.")

'''



# for문

'''

# print("대기번호 : 1")
# print("대기번호 : 2")
# print("대기번호 : 3")
# print("대기번호 : 4")
# print("대기번호 : 5")      # 아래코드와 동일한 결과값을 가진다.

# for waiting_num in [1, 2, 3, 4, 5]:
#     print("대기번호 : {0}".format(waiting_num))

# for waiting_num in range(1, 6):   # 위와 동일한 값이 나온다.
#     print("대기번호 : {0}".format(waiting_num))

starbucks = ["아이언맨", "스파이더맨", "토르", "그루트"]
for customer in starbucks:
    print("{0}, 커피가 준비되었습니다.".format(customer))

'''


# while문

'''

# customer = "토르"
# index = 5
# while index >=1:
#     print("{0}, 커피가 준비되었습니다. {1} 번 남았어요.".format(customer, index))
#     index -= 1
#     if index ==0:
#         print("커피는 폐기처분되었습니다.")

# customer = "아이언맨"
# index = 1
# while True:
#     print("{0}, 커피가 준비되었습니다. 호출 {1}회".format(customer, index))
#     index += 1

customer = "토르"
person = "Unkown"

while person != customer :
    print("{0}, 커피가 준비되었습니다.".format(customer))
    person = input("이름이 어떻게 되나요?")
    if person == "토르":
        print("커피 맛있게 드세요.")
    else :
        print("조금만 더 기다려 주세요")     # 내가 추가해서 만들어 본 코드!

'''

# continue 와 break

'''

absent = [2, 5]  # 결석
no_book = [7, 15, 25]   # 책을 안가지고 온 학생

for student in range(1, 31):   # 1번부터 30번까지 있음
    if student in absent:
        continue
    elif student in no_book:
        print("오늘 수업 여기까지. {0}번 교무실로 따라와".format(student))
        break
    print("{0}번, 책을 읽어봐".format(student))

'''

# 한 줄 for문

'''

# 출석번호 1~9번 까지 있는데, 앞에 100을 붙이기로 했음.

# students = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(students)
# students = [i+100 for i in students]
# print(students)

# 학생 이름을 길이로 변환
# students = ["Do", "Hyeon", "Cheoll", "Thor"]
# students = [len(i) for i in students]
# print(students)

# 학생 이름을 대문자로 변환
students = ["Do", "Hyeon", "Cheoll", "Thor"]
students = [i.upper() for i in students]
print(students)

'''

# 퀴즈

'''
당신은 Cocoa 서비스를 이용하는 택시 기사이다.
50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.

조건 1 : 승객별 운행 소요 시간은 5 ~ 50분 사이의 난수로 정해짐
조건 2 : 당신은 소요시간 5 ~ 15분 사이의 승객만 매칭해야한다.

출력문 예제
[O] 1번째 손님 (소요시간 : 15분)
[ ] 2번째 손님 (소요시간 : 50분)
[O] 3번째 손님 (소요시간 :5분)
...
[ ] 50번째 손님 (소요시간 : 16분)

총 탑승 승객 : 2 분
'''

from random import *
customer = 0  # 총 탑승 승객 수
for i in range(1, 51):    # 1 ~ 50
    time = randrange(5, 51)   # 5 ~ 50
    if 5 <= time <= 15 :   # 매칭 성공
        print("[O] {0}번째 손님 (소요시간 : {1}분".format(customer, time))
        customer += 1
    else :   # 매칭 실패
        print("[ ] {0}번째 손님 (소요시간 : {1}분".format(customer, time))

print("총 탑승 승객 : {0}분".format(customer))