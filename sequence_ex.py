#문자열 : 시퀀스 모델

#연결 : +
print("Py"+"thon")

#반복 : *
print("Python"*3)

#길이 반환
print(len("Python"))

print()
#포함여부 확인 : in 연산자
s = "Python"
#시퀀스 내에 y가 있습니까?
print("y" in s)
#시퀀스 내에 j가 포함되어 있지 않습니까?
print("j" not in s)
print()

#시퀀스 모델의 인덱스 접근
#o를 인덱스로 접근
print(s[4])
#o를 역인덱스로 접근해보겠습니다.
print(s[-2])

#시퀀스 모델의 추출 [1]부터 [5]까지
print(s[1:5])
print(s[-5:-1])