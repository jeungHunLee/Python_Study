import sys

a = input()     # input 내장 함수

# sys.stdin.readline 입력
# 정수 하나 입력
b = int(sys.stdin.readline())

# 정수 여러개 입력
A, B, C = map(int, sys.stdin.readline().split())

# 여러 개의 정수를 한 줄에 입력 받아 리스트에 저장하기
c = list(map(int, sys.stdin.readline().split()))