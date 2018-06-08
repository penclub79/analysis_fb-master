#피클 사용을 위해 pickle을 임포트
import pickle

#피클로 객체 저장
def pwrite01():
    f = open("./sample/players.bin", "wb")  #   b모드(바이너리모드)
    data = {"baseball":9}
    pickle.dump(data, f)
    f.close()

#pwrite01()

def pread01():
    f = open("./sample/players.bin", "rb")  #   b모드(바이너리모드)
    data = pickle.load(f)
    f.close()
    print(data, type(data))

#pread01()

def pwrite02():
    #복수의 객체 저장
    with open("./sample/players.bin", "wb")as f:
        pickle.dump({"baseball": 9}, f, 1)   # protocol 1
        pickle.dump({"basketball": 5}, f, 2)    #protocol 2
        pickle.dump({"soccer": 11}, f, pickle.HIGHEST_PROTOCOL)

pwrite02()

def pread02():
    #복수의 객체 읽기
    with open("./sample/players.bin", "rb") as f:
        print(pickle.load(f))   #파일 포인터를 넘기기 f
        print(pickle.load(f))   #무식한 방법이라하신다
        print(pickle.load(f))
        print(pickle.load(f))   #3개만 읽어야하는데 더이상 읽을게 없어서 EOFError가 뜬다 <- 잡아줘야함

#pread02() EOFError

def pread03():
    
    with open("./sample/players.bin", "rb") as f:
        data_list = []
        while True:
            try:
                data = pickle.load(f)
            except EOFError: #에러가 나면 루프 탈출
                break

            data_list.append(data)

        print(data_list)
pread03()