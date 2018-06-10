# 문제7.
# 문자열을 입력 받아, 해당 문자열을 문자 순서를 뒤집어서 반환하는 함수 reverse(s)을 작성하세요.

st = input('입력>')
for i in st:
    i = st.strip()
print ('결과>'+''.join(reversed(i)))

# s = 'java'
# s = s.strip()
# print(s)