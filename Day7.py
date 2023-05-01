# 표준 입출력

'''

#print("python", "Java", "JavaScript", sep=" vs ")   # sep 는 두 단어 사이의 구분자
# print("python", "Java", sep=" vs ", end="? ")
# print("무엇이 더 재밌을까요?")   # end가 들어감으로 한줄로 표시할 수 있음 (줄바꿈 대신 ?를 넣는거임)

# import sys
# print("Python", "Java", file=sys.stdout)   # 표준 출력
# print("Python", "Java", file=sys.stderr)   # 표준 에러

# 시험성적
# scores = {"수학":0, "영어":50, "코딩":100}
# for subject, score in scores.items():
#     #print(subject, score)
#     print(subject.ljust(8), str(score).rjust(4), sep=":")   # 8칸의 공간을 확보한 후 왼쪽 정렬 / 4칸의 공간을 확보한 후 오른쪽 정렬

# 은행 대기 순번표

# for num in range(1, 21):
#     print("대기번호 : " + str(num).zfill(3))   # 3칸의 공간을 확보한고 나머지 공간에는 0으로 채워 달라는 뜻

answer = input("아무 값이나 입력하세요. : ")
print("입력하신 값은 " + answer + "입니다.")   # 숫자로 출력하기 원할때는 answer 앞에 str 사용해주는 것이 좋음

'''


# 다양한 출력 포맷

'''

# 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
print("{0: >10}".format(500))

# 양수일땐 +로 표시, 음수일 땐 -로 표시
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))       # print("{0: >10}".format(500)) 여기에서 500대신 -500을 적어도 음수가 찍히지만 양수일때 +가 없음

# 왼쪽 정렬하고, 빈칸을 _로 채움
print("{0:_<+10}".format(500))

# 3자리 마다 콤마를 찍어주기
print("{0:,}".format(99999999999999999999))

# 3자리 마다 콤마를 찍어주는데, +,- 부호도 사용
print("{0:+,}".format(99999999999999999))
print("{0:+,}".format(-99999999999999999))

# 3자리 마다 콤마를 찍어주며, 부호도 사용하고, 자릿수 확보하기, 공백은 ^ 으로 채우기
print("{0:^<+30,}".format(999999999999))

# 소수점을 출력하는 방법
print("{0:f}".format(5/3))

# 소수점을 특정 자리수까지만 출력해주는 방법
print("{0:.3f}".format(5/3))   # 소수점 4째 자리에서 반올림 해달라는 뜻

'''


# 파일 입출력

'''

# score_file = open("score.txt", "w", encoding="utf8")    # 쓰기
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# print("코딩 : 100", file=score_file)
# score_file.close()

# score_file = open("score.txt", "a", encoding="utf8")   # 추가하기
# score_file.write("과학 : 70")
# score_file.write("\n국어 : 90")
# score_file.close()

score_file = open("score.txt", "r", encoding="utf8")     # 불러오기
# print(score_file.read())  # 파일 전체를 읽어오기

# print(score_file.readline())    # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동 (프린트는 자동으로 줄바꿈 줄바꿈 안하고 싶을때 end="")
# print(score_file.readline())
# print(score_file.readline())
# print(score_file.readline())

# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line)    # end 사용하면 줄 바꿈 없어짐

lines = score_file.readlines()   # list 형태로 저장함
for line in lines:
    print(line, end="")

score_file.close()

'''


# Pickle

'''

import pickle

# profile_file = open("profile.pickle", "wb")   # b는 바이너리, pickle에서는 인코딩이 필요없음
# profile = {"이름":"도현철", "나이":27, "취미":["축구", "독서", "피아노연주"]}
# print(profile)
# pickle.dump(profile, profile_file)    # profile에 있는 정보를 file에 저장하는 것
# profile_file.close()

profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file)   # file에 있는 정보를 profile 에 불러오기
print(profile)
profile_file.close()

'''


# with

'''

# import pickle
# with open("profile.pickle", "rb") as profile_file:
#     print(pickle.load(profile_file))

# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요.")

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())   # close가 필요없다는 장점이 있음

'''


# 퀴즈

'''
당신의 회사에서는 매주 1회 작성해야 하는 보고서가 있습니다.
보고서는 항상 아래와 같은 형태로 출력되어야 합니다.

- X 주차 주간보고 -
부서 : 
이름 :
업무 요약 :

1주차부터 50주차 까지의 보고서 파일을 만드는 프로그램을 작성하시오.

조건 : 파일명은 "1주차.txt", "2주차.txt", ... 와 같이 만든다.
'''

for i in range(1,51):
    with open(str(i) + "주차.txt", "w", encoding="utf8") as report_file:
        # report_file.write("-" + str(i) + "주차 주간보고 -") 내가 한 답
        report_file.write("- {0} 주차 주간보고 -".format(i))
        report_file.write("\n부서 : 디지털트윈사업본부")
        report_file.write("\n이름 : 도현철")
        report_file.write("\n업무 요약 : 3차원 지도 제작")