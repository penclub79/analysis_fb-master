#논리합 (or) : 둘 중 하나면 True면 true
a=2
b=3

print(a % 2 == 0 or b % 3 == 0)

#논리곱 (and) : 둘 다 True여야 True
print(a > 0 and b < 0)

#논리 부정 (not) : 논리값을 반대로 True -> false, False -> true
print(a > 10)   #사실상 False
print(not a > 10)
print(not(a % 2 == 0 and b % 3 == 0))#일괄 부정