money = [50000, 10000, 5000, 1000, 500, 100, 50, 10, 5, 1]

a = input('돈을 입력하세여 : ')

a = int(a)

for i in money:
    count = a // i
    a -= i*count
    print ('{0}원: {1}개'.format(i, count))




