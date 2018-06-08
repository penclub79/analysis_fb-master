num = input('정수를 입력하세요 : ')

if num.isdigit():
    if int(num) % 3 == 0:
        print('홀수입니다.')
    else:
        print('짝수입니다.')

