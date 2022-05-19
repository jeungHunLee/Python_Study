# sys 라이브러리
import sys
print(sys.argv)     # 대화형 인터프리터에서 파이썬 파일명 뒤에 인자 입력시 리스트 형태로 반환

# pickle
# 파일 저장
import pickle
f = open("test.txt", 'wb')  # 바이너리 모드로 쓰기
data = ['you', 'need', 'Python']
pickle.dump(data, f)    # 저장

# 파일 읽기
f = open("test.txt", 'rb')    # 바이너리 모드로 읽기
data = pickle.load(f)
print(data)

# time
import time
print(time.time())    # 현재 시간을 실수 형태로 반환
print(time.localtime(time.time()))  # time.time()의 실수 값을 년,월,일,시,분,초로 반환
print(time.asctime(time.localtime(time.time()))) # tome.licaltime의 튜플 값을 좀 더 알바보기 쉽게 반환
print(time.ctime) # time.asctime과 같은 값 반환

# random
import random
print(random.randim())   # 0과 1사이의 난수 발생
print(random.randint(1, 10))      # 1에서 10 사이의 난수 발생
