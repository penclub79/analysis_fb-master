def try_f1():
    try:
        lst = [1, 3, 5, 7, 9]
        lst[5]  #IndexError
    except:
        print("Error")

#try_f1() 에러남

def try_f2():
    try:
        value = int("10a") #ValueError
    except ValueError as e: 
        print("변환할 수 없습니다.")
    except Exception as e:
        print("Exception e:", e)
        print("type e:", type(e))


#try_f2() 에러남

def try_f3():
    result= 4/0 #ZeroDivisionError

#try_f3()

def example():  #키보드로 부터 숫자를 입력받아서 에러상황 만듬
    num1 = input("첫 번째 숫자를 입력해 주세요 : ")
    num2 = input("두 번째 숫자를 입력해 주세요 : ")

    try:
        num1 = int(num1)    #int로 변환한다
        num2 = int(num2)    #int로 변환한다
        result = num1 / num2
    except ValueError as e:
        print("정수형이 아닙니다.")
    except ZeroDivisionError as e:
        print("0으로는 나눌수 없어요.")
    except Exception as e:
        print("e:", e)
    else:   #오류가 없을 때만 실행
        print("{} / {} = {}".format(num1, num2, num1 / num2))
    finally:    #오류 여부 상관 없이 마지막에 실행
        print("예외처리 완료")
    
#example()           # 숫자만 입력하면 정상적인 상황

#특정경우에는 일부러 예외를 발생시키기도 합니다.
def beware_dog(animal):
    if animal == "dog":
        #예외발생   #예외는 자기가 만들수도 잇음
        raise RuntimeError("멍멍")
    else:
        print("어서오세요")
try:
    beware_dog("cow")
    beware_dog("cat")
    beware_dog("dog")
except RuntimeError as e:       #as키워드 : 이름 변경하고자 할때 예외처리, 모듈에서도 쓰인다. 봐두센
    print(e)
    print(type(e))