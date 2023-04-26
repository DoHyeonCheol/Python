# 문자열

# sentence = '나는 소년입니다'
# print(sentence)

# sentence2 = """
# 나는 소년이고,
# 파이썬은 쉽고
# 열심히 하고 있어요
# """
# print(sentence2)


# 슬라이싱
# jumin = "990120-1234567"

# print("성별 : " + jumin[7])  # 인덱스는 1부터 시작이 아니라 0부터 시작
# print("출생 연도 : " + jumin[0:2])  # 0에서 2까지가 아닌 0에서 2 직전까지를 불러옴
# print("출생 월 : " + jumin[2:4])
# print("출생 일 : " + jumin[4:6])
# print("생년월일 : " + jumin[:6])   # 0을 안적으면 처음부터 6직전까지 불러온다를 의미

# print("뒤 7자리 : " + jumin[7:14])
# print("뒤 7자리 : " + jumin[7:])  # 끝 자리를 비워두면 끝까지 불러오는것을 의미
# print("뒤 7자리 : " + jumin[-7:])  # -를 사용하면 뒤에서부터 불러오는 것을 의미

# 문자열 처리함수

# python = "Python is Amazing"
# print(python.lower())  # 전부다 소문자로 출력
# print(python.upper())  # 전부다 대문자로 출력
# print(python[0].isupper())  # python변수의 인덱스 0번째 자리가 대문자인 것이냐고 물어보는 것 (True)
# print(python[0].islower())  # python변수의 인덱스 0번째 자리가 소문자인 것이냐고 물어보는 것 (False)
# print(len(python))   # python변수의 문자열의 길이를 알려줌
# print(python.replace("Python", "Java"))  #python 변수안에 있는 Python을 찾아 Java로 변환

# index = python.index("n")  #python변수 안에 n이 있는 위치 찾기
# print(index)
# index = python.index("n", index + 1)  # 두번째 n을 찾는 방법
# print(index)

# print(python.find("n"))
# # print(python.find("Java"))  #결과값이 -1이 나옴 (값이 포함되지 않았을때 -1이나옴)
# # print(python.index("Java"))  #결과값이 나오지 않고 오류가 남
# print(python.count("n"))  # n이 나오는 횟수 알려줌

# 문자열 포맷

# print("a" + "b")  #ab
# print("a", "b")   #a b

# 방법 1

# print("나는 %d살 입니다." % 27)    # %d는 %뒤에 있는 숫자를 그 자리에 넣겠다는 뜻임(d는 정수를 의미함)
# print("나는 %s을 좋아해요." % "Python")   #s는 문자열을 의미
# print("Apple은 %c로 시작해요." % "A")  # c는 한 글자를 의미
# # %s는 문자, 정수 다 필요없이 가능하다는 것이 특징
# print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))   #차례대로 넣어서 결과값 도출

# 방법 2

# print("나는 {}살입니다.".format(20))
# print("나는 {}색과 {}색을 좋아해요." .format("파란", "빨간"))
# print("나는 {1}색과 {0}색을 좋아해요." .format("파란", "빨간"))  # format 뒤 괄호에 있는 단어의 순서를 0번부터 시작해서 확인하는 방법임

# 방법 3

# print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 20, color="빨간"))
# print("나는 {age}살이며, {color}색을 좋아해요.".format(color="빨간", age = 20))

# 방법 4 (ver 3.6 이상부터 가능)

# age = 20
# color = "빨간"
# print(f"나는 {age}살이며, {color}색을 좋아해요.")


# 탈출문자

# print("백문이 불여일견 \n백견이 불여일타")  # \n은 줄바꿈을 나타내는 것임
# print("저는 '도현철' 입니다.")
# print('저는 "도현철" 입니다.')  # '' or ""는 사용불가능
# print("저는 \"도현철\" 입니다.")
## \\ : 문장 내에서는 \로 인식
# print("C:\\Users\\sybae\\PycharmProjects\\Python Basic")

## \r : 커서를 맨 앞으로 이동
# print("Red Apple\rPine")

## \b : 백스페이스 (한 글자 삭제)
# print("Redd\bApple")

## \t : 탭 (띄어쓰기)
# print("Red\tApple")


'''
QUIZ
사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오

예) http://naver.com
규칙1 : http:// 부분은 제외 >>> naver.com
규칙2 : 처음 만나는 점(.) 이후 부분은 제외 >>>> naver
규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!"로 구성
                nav               5           1             !
예) 생성된 비밀번호 : nav51!
'''

# url = "http://naver.com"
# My_url = url.replace("http://", "")  # 규칙 1
# My_url = My_url[:My_url.index(".")]  # 규칙 2
# Pass = My_url[0:3] + str(len(My_url)) + str(My_url.count("e")) + str("!")
# print("{0} 의 비밀번호는 {1} 입니다.".format(url, Pass))

url = "http://google.com"
My_url = url.replace("http://", "")  # 규칙 1
My_url = My_url[:My_url.index(".")]  # 규칙 2
Pass = My_url[0:3] + str(len(My_url)) + str(My_url.count("e")) + str("!")
print("{0} 의 비밀번호는 {1} 입니다.".format(url, Pass))