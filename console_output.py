

#print 함수 안에 출력할 내용을 인자값을 전달
print(2018)
print(3.141592)
print("Hello Python")


#여러 내용의 연속 출력: ,로 연결
print ("Hello", "Python")

#문자열을 합쳐 출력할 때: +로 연결
print("Hello"+" "+"Python")

#문자열 반복 출력 : * 갯수
print("Python" * 3)

print()

# 문자열과 다른 형식을 +했을 경우
# print(3+"Python") 에러
#Solution : 형변환 시도
print(str(3)+"Python")

#구분자 sep, end 변경
print("신호철", "공부중", sep=":", end="")  #,로 구분, 개행 안함
#강제로 end로 인해서 개행을 막았다.
print("추가 문자열")

