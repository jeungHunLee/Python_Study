# ndarray 연산
import numpy as np

# 요소 간의 연산
a = np.array([[20, 30],
              [40, 50]])

b = np.array([[1, 2],
              [3, 4]])

c = a + b    # 행렬의 각 요소를 더함
print(c)
'''[[21 32]
 [43 54]]'''

d = a - b    # 행렬의 각 요소를 뺌
print(d)
'''[[19 28]
 [37 46]]'''

e = a * b    # 행렬의 각요소를 곱
print(e)
'''[[ 20  60]
 [120 200]]'''

# 행렬간 연산
a = np.array([[1, 2, 3],
              [4, 5, 6]])

b = np.array([[1, 2],
             [3, 4],
             [5, 6]])

c = np.dot(a, b)    # 행렬 a, b의 곱
print(c)
'''[[22 28]
 [49 64]]'''

# 요소 추가
a = np.array([1, 2, 3])
a = np.append(a, 4)    # axis=None 마지막 위치에 추가
print(a)
'''[1 2 3 4]'''

a = np.array([[1, 2, 3], [4, 5, 6]])
a = np.append(a, [[7, 8, 9]], axis=0)    # axis=0 축으로 [[7, 8, 9]] 추가
print(a)
'''[[1 2 3]
 [4 5 6]
 [7 8 9]]'''

a = np.array([[1, 2, 3], [4, 5, 6]])
a = np.append(a, [[7], [8]], axis=1)    # axis=1 축으로 [[7], [8]] 추가
print(a)
'''[[1 2 3 7]
 [4 5 6 8]]'''

# 요소 삽입
a = np.array([1, 2, 3])
a = np.insert(a, 1, 4)    # index == 1에 4 추가
print(a)    # [1 4 2 3]

a = np.array([[1, 2, 3],
              [4, 5, 6]])
a = np.insert(a, 1, -1, axis=0)    # index == 1에 axis=0 축 방향으로 [-1, -1, -1] 삽입
print(a)
'''[[ 1  2  3]
 [-1 -1 -1]
 [ 4  5  6]]'''

a = np.array([[1, 2, 3],
              [4, 5, 6]])
a = np.insert(a, [0, 2], [0, 0, 0], axis=0)    # index == 0, index == 2에 axis=0 축 방향으로 [0, 0, 0] 삽입
print(a)
'''[[0 0 0]
 [1 2 3]
 [4 5 6]
 [0 0 0]]'''

a = np.array([[1, 2, 3],
              [4, 5, 6]])
a = np.insert(a, [0, 2], [[-1], [-1]], axis=1)    # index == 0, index == 2 앞에 axis=1 축 방향으로 [-1, -1] 각각 삽입
print(a)
'''[[-1  1  2 -1  3]
 [-1  4  5 -1  6]]'''

# 요소 제거
a = np.array([[1, 2, 3],
              [4, 5, 6]])
a = np.delete(a, 0, axis=0)    # index == 0, axis=0 축방향으로 삭제
print(a)    # [[4 5 6]]

a = np.array([[1, 2, 3],
              [4, 5, 6]])
a = np.delete(a, 1, axis=1)    # index == 2, axis=1 축방향으로 삭제
print(a)
'''[[1 3]
 [4 6]]'''

# shape 속성 변경
a = np.arange(12)
a.shape = (3, 4)
print(a)
'''[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]'''
b = a.reshape(3, 4)
print(b)
'''[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]'''

# 1차원으로 풀기(ravel())
a = np.arange(24).reshape(3, 4, 2)
print(a)
'''[[[ 0  1]
  [ 2  3]
  [ 4  5]
  [ 6  7]]

 [[ 8  9]
  [10 11]
  [12 13]
  [14 15]]

 [[16 17]
  [18 19]
  [20 21]
  [22 23]]]'''

b = a.ravel()
print(b)    # [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23]
