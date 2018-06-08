# point.py

#클래스 만들기
class Point:
    instance_count = 0  #클래스 영역  (인스턴스 영역아닙니다.)

    #생성자
    def __init__(self, x = 0, y = 0):
        self.x, self.y = x, y
        #클래스 영역의 접근
        Point.instance_count += 1


    #소멸자
    def __del__(self):
        Point.instance_count -= 1

    #__str__ 구현   사용자용
    def __str__(self):
        return "Point x = {}, y = {}".format(self.x, self.y)

    #__repr__구현   개발자용
    def __repr__(self):
        return "Point({}, {})".format(self.x, self.y)

    # 인스턴스 메서드
    def setX(self, x):
        self.x = x

    def getX(self):
        return self.x

    def setY(self, y):
        self.y = y

    def getY(self):
        return self.y

def bound_method():
    p = Point() # 객체 생성
    p.setX(10)
    p.setY(10)

    print(p.getX(), p.getY(), sep = ",")
    print(p.getX, p.getY)

def unbound_method():
    p = Point()
    Point.setX(p, 10) #(self값 지정, 10)
    Point.setY(p, 10)
    print(Point.getX(p), Point.getY(p), sep=",")
    print(Point.getX, Point.getY)

if __name__ == "__main__":
    bound_method()
    unbound_method()    #<function Point.getX at 0x00000045EDE701E0> 함수를 객체화 했다.
