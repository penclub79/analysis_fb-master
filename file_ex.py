def write01():
    #텍스트 파일 쓰기
    f = open('./sample/test.txt', 'w', encoding="utf-8")
    size = f.write("Life is too short, you need Python")   #내용을 쓰고 길이를 반환
    print("write size : {}".format(size))
    f.close()   #열었으면 꼭 닫아 줍시다

#write01()

def read01():
    #텍스트 파일 읽기
    f = open("./sample/test.txt", 'r', encoding="utf-8")
    text = f.read()
    print(text)
    f.close

#read01()

def write02():
    #여러줄을 만들어 봅시다
    f = open("./sample/multilines.txt", 'w', encoding="utf-8")
    for i in range(1, 10):
        f.write("Line %d\n" % i)
    f.close

# write02()

def read02():
    f = open("./sample/multilines.txt", 'r', encoding="utf-8")
    text = f.read()
    print(text)
    f.close()

#read02()    
#메모리를 통채로 읽어오기때문에 Line단위로 끊어서 읽어오자

def read02_1():
    f = open("./sample/multilines.txt", 'r', encoding="utf-8")
    #루프를 돌면서 한줄씩 읽어와 보자
    while True:
        line = f.readline()
        if not line:    #읽을 라인이 없다면 break
            break
        print(line) #end로 하면 개행이 일어나지 않는다
    f.close()

# read02_1()

def read02_2():
    f = open("./sample/multilines.txt", 'r', encoding="utf-8")
    lines = f.readlines()
    print(lines)
    line = lines[5]
    print(line)
    f.close()

#read02_2()  
#적당한 크기의 파일사이즈를 할때 좋음. 크기가 크면 메모리 부담이 간다

'''
sample 디렉토리 안에 sangbuk.csv 파일을 열고
각 줄을 dict으로 만들고 리스트에 저장해 봅시다
'''

def slamdunk():
    members = []
    
    f = open("./sample/sangbuk.csv", 'r', encoding="utf-8")
    while True:
        line = f.readline() #한줄씩 읽어올거여
        if not line:
            break
        line = line.strip().replace(" ","") #공백 문자를 없애고 중간의 공백문자도 없애자
        info = line.split(",")  #,로 구분자를 나눠본다
        member = {"name":info[0], "number": info[1],
                     "height": info[2], "position":[3]}
        members.append(member)

    print(members)
    f.close()
slamdunk()  #window라서 cp949로 저장된 파일이다.

#바이너리 파일 다루기 모드 : b
def binfile():
    f_src = open("./sample/rose-flower.jpeg", "rb")
    data = f_src.read()
    f_src.close()

    f_dest = open("./sample/rose-flower-copy.jpeg", "wb")   #사진 파일을 복사해서 집어넣었다
    f_dest.write(data)
    f_dest.close()

#binfile()

def safe_file():
    #파일은 open하면 반드시 닫아줘야 하는데
    #with ~ as를 이용하면 파이썬이 사용 후 닫아준다

    with open('./sample/multilines.txt', 'r') as f:
        for line in f.readlines():      #모든 줄을 스트링 배열로 변환
            print(line, end="") #개행 없애기

    print()
    #f가 닫혀 있는지 확인
    print(f.closed) #닫혀있는지 확인하는건 closed이다

safe_file()
