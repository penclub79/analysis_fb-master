str = "Life is too short, You need Python"
print(str.split())
a = str.split()
print("알파뱃 : ", a)
print("총 몇개의 알파뱃 글자를 사용했나? ", len(a))

#소문자 변경
a = str.lower()
print("소문자로 변경 = ", a)

#공백과 ,를 제거
a.split()
a = a.split(",", 2)
print(a)
print("".join(a))
print()

#문자열을 list로 형변환
lst = list("".join(a))
print(lst)


