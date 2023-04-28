# 함수

'''

def open_account():
    print("새로운 계좌가 생성되었습니다.")

open_account()

'''


# 전달값과 반환값

'''

def open_account():
    print("새로운 계좌가 생성되었습니다.")

def deposit(balance, money):  # 입금
    print("입금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance + money))
    return balance + money

def withdraw(balance, money):   # 출금
    if balance >= money:    # 잔액이 출금금액보다 많을때
        print("출금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance - money))
        return balance - money
    else :
        print("출금이 실패하였습니다. 잔액은 {0}원 입니다.".format(balance))
        return balance

def withdraw_night(balance, money):  # 저녁에 출금
    commission = 100  # 수수료 100원
    return commission, balance - money - commission

balance = 0   # 현재 잔액
balance = deposit(balance, 10000)
# balance = withdraw(balance, 20000)   # 출금 실패
# balabce = withdraw(balance, 5000)      # 출금 성공
commission, balance = withdraw_night(balance, 5000)
print("수수료는 {0}원이며, 잔액은 {1}원입니다.".format(commission, balance))

'''


# 기본값

'''

# def profile(name, age, main_lang):
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어 :{2}".format(name, age, main_lang))   # 줄바꿈 할때는 \를 사용할것
# profile("유재석", 20, "Python")
# profile("김태호", 27, "Cpp")

# (만약 같은 학교 같은 학년 같은 반 같은 수업을 듣는 학생)

def profile(name, age=17, main_lang= "Python"):
    print("이름 : {0} \t 나이 : {1} \t 주 사용 언어 :{2}".format(name, age, main_lang))

profile("유재석")
profile("김태호")
profile("강호동")

'''


# 키워드 값

'''

def profile(name, age, main_lang):
    print(name, age, main_lang)

profile(name = "유재석", main_lang = "Python", age = 27)
profile(age = 31, main_lang = "Java", name = "강호동")

'''


# 가변인자

'''

def profile(name, age, *language):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()


# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
#     print(lang1, lang2, lang3, lang4, lang5)  # 기존 방식

profile("유재석", 20, "Python", "Java", "C", "Cpp", "C#", "JavaScript")
profile("김태호", 25, "Kotlin", "Swift", "", "", "")

'''


# 지역변수와 전역변수 (지역변수 : 함수 내에서만 쓸 수 있는 것 , 전역변수 : 프로그램 내 어디서든 쓸 수 있는것)

'''

gun = 10

def checkpoint(soldiers):  # 경계근무
#    gun = 20       # 지역변수
    global gun      # 전역변수 (전역 공간에 있는 gun 사용)
    gun = gun - soldiers
    print("[함수 내] 남은총 : {0}".format(gun))

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은총 : {0}".format(gun))
    return gun

print("전체 총 : {0}".format(gun))
#checkpoint(2)  # 경계 근무 2명이 나감
gun = checkpoint_ret(gun, 2)
print("남은 총 : {0}".format(gun))

'''


# 퀴즈

'''
표준 체중을 구하는 프로그램을 작성하시오

* 표준 체중 : 각 개인의 키에 적당한 체중

(성별에 따른 공식)
남자 : 키(m) x 키(m) x 22
여자 : 키(m) x 키(m) x 21

조건 1) 표준 체중은 별도의 함수 내에서 계산
    - 함수명 : std_weight
    - 전달값 : 키(height), 성별(gender)

조건 2) 표준 체중은 소수점 둘째자리까지 표시

(출력 예제)
키 181cm 남자의 표준 체중은 72.07kg 입니다.
'''

def std_weight(height, gender):
    if gender == "남자":
        return height * height * 22
    else:
        return height * height * 21

height = 181
gender = "남자"
weight = round(std_weight(height / 100, gender), 2)    # round는 반올림
print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))