name = input('정수를 입력하세요 : ')


if name.isdigit() :
    if int(name) % 3 == 0:
        print('3의 배수 입니다.')
    else :
        print('3의 배수가 아닙니다.')
else:
    print('정수가 아닙니다.')
