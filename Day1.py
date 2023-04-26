# 숫자형 데이터 (정수, 실수 모두 가능)
'''
print (5)
print(-10)
print(3.14)
print(100+35)
print(9*30)
print(3*(40+7))
'''

# 문자열 자료
'''
print('풍선')
print("나비")
print("가"*9)   #정수형 + 문자열 자료 함께 사용
'''
# Bollean 자료형 ( 참 / 거짓을 나타내는 자료형)
#
# print(5>10)
# print(5<10)
# print(True)
# print(False)
# print(not True) #not을 사용하면 뒤에 나오는 것과 반대되는 결과값을 표현
# print(not (5>10))

# 변수 (ex. 애완동물을 소개해주세요)
#
# animal = "강아지"
# name = "연탄"
# age = 4  # 정수형이기에 ""없음
# hobby = "산책"
# is_adult = age >=3
#
# print("우리집" + animal + "의 이름은 "+ name + "이예요")
# # hobby = "공놀이"  #이렇게 진행한다면 산책이 아니라 공놀이로 변할 것임 더 이후에 나온 것으로 받아드리며, 중간에 넣을수도 있다는 것)
# print(name + "이는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요")
# #print(name, "이는 ", age, "살이며, ", hobby, "을 아주 좋아해요") # +가 아닌 ,를 사용한다면 무조건 띄어쓰기가 된다
# print(name + "이는 어른일까요? " + str(is_adult))

# Ctrl + / 사용하면 드래그한 모든 줄 주석처리 반대일 경우 주석 풀기

# Quiz) 변수를 이용하여 다음 문장을 출력하시오.

# 1. 변수명 : station
# 2. 변수값 : "사당", "신도림, "인천공항" 순서대로 입력
# 3. 출력 문장 : XX 행 열차가 들어오고 있습니다.

station = "사당"
print(station + "행 열차가 들어오고 있습니다.")
station = "신도림"
print(station + "행 열차가 들어오고 있습니다.")
station = "인천공항"
print(station + "행 열차가 들어오고 있습니다.")
