#internal_mod.py

#sys 모듈
#파이썬 이터프리터 관련 정보와 기능
#argv

import sys

def argsv_f():
    print(sys.argv)
    args = sys.argv[1:]
    print("args : ", args)

# 환경 관련 내용들
def env_f():
    # 플랫폼 정보를 얻어온다
    print(sys.platform)
    # 시스템 버전을 얻어온다
    print(sys.version)
    # 모듈 디렉토리 확인        append로 path(환경변수)에 추가할 수 있다.
    print(sys.path)

env_f()

# random 모듈

# 임의의 특정 값을 선택 제공
# 그 이외에 난수관련 유틸리티 함수

import random

# 0 ~ 1 사이의 난수 발생
print(random.random())
# 특정 범위의 정수 내에서 난수(정수)발생
print(random.randint(1, 6))

# 랜덤 유틸리티 함수
seq = ["짬뽕", "짜장면", "짬짜면"]
# 이 리스트를 섞어 봅시다 : shuffle
random.shuffle(seq)
print(seq)

# 순차형에서 임의의 한개 객체 반환 : choice
print(random.choice(seq))

#Sampling
print(random.sample(range(1, 46), 6))   # 1 ~ 45 사이의 순차 정수 중에서 6개를 추출