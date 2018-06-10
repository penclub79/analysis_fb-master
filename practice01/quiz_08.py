keys =[]
s = 0
for key in range(0, 5):
    key = input("정수 입력 : ")
    keys.append(int(key))

print ('평균 : {}'.format(sum(keys, 0)/len(keys)))



# l = []
#
# s = 0
#
# while len(l) != 5:
#
#     n = input('>')
#
#     if n.isdigit() is False:
#
#         print('Error: is not digit')
#
#         continue
#
#     l.append(int(n))
#
#
#
# print(sum(l, 0)/len(l))

