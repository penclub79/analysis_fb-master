# 조건문 if ~ elif ~ else

n = -2

if n > 0:
    print("양수")
elif n < 0:
    print("음수")
else:
    print("0")
# if는 중첩사용 가능
# 조건이 여러개일 경우 : and, or 등 논리연산자를 이용해서 조건을 조합하자

# 조건 표현식
# Java, C의 3항 연산과 비슷
money = 12000
print("택시 타자" if money >= 10000 else "버스 타자")

money = 0
print("택시 타자" if money >= 10000 else "걸어감" if money == 0 else "버스 타자")

#in, not in : 포함 관계를 나타내는 연산
#리스트 내포도 같이 해보자
source = [x for x in range(1, 100, 2)] #리스트 내포
# 1~ 100까지 2씩 증가

if 2 in source:
    print("2를 포함하고 있습니다.")
else:
    print("2를 포함하고 있지 않습니다.")

