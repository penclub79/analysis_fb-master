#paint.py
#point를 임포트 하여 사용
from point import Point #모듈명은 point 불러와야할 객체는 Point
#point 모듈로 부터 Point를 불러온다

p1 = Point(10, 10)
print("p1", p1)
#repr 메시지를 확인
print("repr : ", repr(p1))
print("instance count:", Point.instance_count)

p2 = Point(20, 20)
print("p2", p2)
#repr 메시지를 확인
print("repr : ", repr(p2))
print("instance count:", Point.instance_count)

p2_copy = eval(repr(p2))    #repr출력 문자로 부터 p2_copy문자열을 만들수 있다.
print("p2_copy : ", p2_copy)

