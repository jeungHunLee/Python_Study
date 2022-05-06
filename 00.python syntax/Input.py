import sys

a = input()     # input 내장 함수

# sys.stdin.readline 입력
# 정수 하나 입력
b = int(sys.sdtin.readline())

# 정수 여러개 입력
A, B, C = map(int, sys.stdin.readline().split())

# 여러개의 정수를 한 줄에 입력 값으로 받아 리스트에 저장하기
l1 = list(map(int, sys.sdtin.readline.split()))

# n줄의 정수를 입력받아 리스트에 저장하기
n = int(sys.sdtin.readline())
l2 = list(sys.stdin.readline().split() for i in range(n))
