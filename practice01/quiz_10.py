# 문제10.
# 주어진 if 문을 dict를 사용해서 수정하세요.

menu = input('메뉴 : ')
keys = ('오뎅', '순대', '만두')
values = (300, 400, 500)
d = dict(zip(keys, values))
print('가격: {}'.format(d[menu]))
