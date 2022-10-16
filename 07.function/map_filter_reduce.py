# map
def two_times(x): return x * 2

print(list(map(two_times, [1, 2, 3, 4])))   # [2, 4, 6, 8]

arr1 = [1, 2, 3, 4]
arr2 = [11, 22, 33, 44]

f = lambda x, y: (x * 2, y * 2)
print(list(map(f, arr1, arr2)))    # [(2, 22), (4, 44), (6, 66), (8, 88)]

# filter
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
f = lambda x: True if x % 2 == 0 else False    # boolean 값 반환
print(list(filter(f, arr)))    # [2, 4, 6, 8, 10]

# reduce
from functools import reduce
arr = [1, 2, 3, 4, 5]
f = lambda x, y: x + y    # x: 0 or 이전 연산의 결과 값 y: iterable 객체의 요소
print(reduce(f, arr))    # 15