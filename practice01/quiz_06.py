data = [1, 3, 5, 8, 9, 11, 15, 19, 18, 20, 30, 33, 31]
s = 0
sum = 0

for data in data:
    if(data % 3 == 0):
        s += 1
        sum += data
print('3의 배수 개수 : ', s)
print('3의 배수 합 : ', sum)

