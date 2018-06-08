#  [[문자형]]
#   시퀀스형
#   변경 불가(immutable) 자료형이에요
str1 = "Life is too short, you need Python"
str2 = "Welcome Python"

#타입 판별
print(type(str1), type(str2))
print()
#instance판변
print(str1, "str?:", isinstance(str1, str))

#여러 줄 문자열
multiline = """
Java
Python
Linux
"""
print(multiline)

#문자열",'사용 사능
#print("I said "Yes"") SyntaxError
#Solution 1: 좋은 방법 아님
print('I said "Yes"')
#Solution 2: 이스케이프 문자(\)를 활용
print("I said \"Yes\"")

#문자열의 인덱싱, 슬라이싱, len
print(len(str1)) #  길이 : len
print(str1[5])   #  문자열의 인덱스 접근: 시퀀스형
print(str1[5:7]) #  슬라이싱
print(str1[5:])  #  생략하면 끝까지
print(str1[:6])  #  앞을 생략하면 처음부터
print(str1[:])   #  앞뒤를 생략하면 시퀀스 전체

#str1[0] = 'l'    #  변경 안됨 - 변경 불가 객체[TypeError]

# [[[대소문자 관련]]]
#   upper()      : 전체 대문자
#   lower()      : 전체 소문자
#   swapcase()   : 대 <-> 소문자 전환
#   capitalize() : 첫 문자 대문자로
#   title()      : 각 단어의 첫글자를 소문자
str3 = str1.lower().title()     #필요한 메서드들을 연결해서 사용할수 있다.(Chaining)
print(str3)

# [[[검색관련]]]
print("count()", str1.count("short"))   #검색어의 갯수
print("find()", str1.find("Python"))    #문자열 내 검색
print("find()", str1.find("Life", 6))   #6번 인덱스부터 Life를 검색
print("rfind()", str1.rfind("Life"))    #우측으로부터 검색

print("find() 없는 값: ", str1.find("Java"))
# 찾는 내용이 없으면 -1을 반환
print("index() : ", str1.index("Python"))
#print("index() 없는 값: ", str1.index("Java"))  #없으면 (ValueError)

# [[[분리와 결합]]]
print("=====분리, 결합=====")
s = "Java and Python"
lines = """\
Java
Python
Linux
Oracle"""

# 분리 : split - ' ' 문자를 기준으로 분리
print(s.split())            #공백 문자 기준 분리
print(s.split(" and "))     #특정 문자열 기준 분리

# 합치기 : join
t = s.split(" and ")
#   : 문자를 넣어서 합쳐 보겠습니다.
print(":".join(t))

s2 = "abc:def:ghi:jkl"
#   : 기준 분리한 후 -> 2개만 가져오기
print(s2.split(":", 2))
print(s2.rsplit(":", 2))

# splitlines() : 개행 문자를 기준으로 분리
print(lines.splitlines())   #문자열에서 개행부분을 \을 막아야 개행이 안일어남.

# [[[판별관련]]]
#   isdigit() : 형태가 숫자 형태인
#   isalpha() : 알파벳 형태인가
#   islower() : 소문자 형태인가
#   isupper() : 대문자 형태인가
#   isspace() : 공백문자 형태인가

num = input("정수를 입력하세요 : ") # 문자열을 입력 받는다
result = num * 2                  # * 반복횟수(시퀀스 반복이 일어난다)
print("result", result)
#Solution 1:
'''
result = int(num) * 2
print("result : ", result)
'''
#Solution 2:
if num.isdigit():
    result = int(num) * 2
else:
    result = "정수가 아니에요."

print("result : ", result)

