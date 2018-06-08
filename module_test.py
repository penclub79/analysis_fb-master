# module test
# 모듈 임포트

import math
import mymod

#이럴 경우는  모듈명을 앞에 붙이고 객체를 사용할 수 있게 됩니다.
print(math.pi)
print(mymod.pi)

r = 10
print("Round : ", math.pi * r ** 2)
print("Round : ", mymod.pi * r ** 2)

#어떤 모듈이 현재 로드되어 있는가
import sys
#현재 로드된 모듈의 목록을 출력\
#print(sys.modules)
#내 모듈은 로드되었는가?

modules = sys.modules.keys()

print("YES" if "mymod" int modules else "NO")

