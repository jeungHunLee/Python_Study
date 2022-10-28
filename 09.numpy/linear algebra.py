# 선형 대수학 관련 함수
import numpy as np

# 단위 행렬 만들기
a = np.eye(3)    # 3 * 3의 단위 행렬 생성
print("a = \n", a)
'''a = 
 [[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]'''

# 역행렬 만들기
b = np.array([[1, 3], [2, 4]])
print("b = \n", b)
'''b = 
 [[1 3]
 [2 4]]'''
print("inverse matrix of b = \n", np.linalg.inv(b))    # 역행렬
'''inverse matrix of b = 
 [[-2.   1.5]
 [ 1.  -0.5]]'''

# 전치행렬
a = np.arange(12).reshape(3, 4)    # 2차원 행렬
print("a = \n", a)
'''a = 
 [[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]'''

print("a.T = \n", a.T)
'''a.T = 
 [[ 0  4  8]
 [ 1  5  9]
 [ 2  6 10]
 [ 3  7 11]]'''

b = np.arange(24).reshape(2, 4, 3)    # 3차원 행렬
print("b = \n", b)
'''b = 
 [[[ 0  1  2]
  [ 3  4  5]
  [ 6  7  8]
  [ 9 10 11]]

 [[12 13 14]
  [15 16 17]
  [18 19 20]
  [21 22 23]]]'''

print("b.T = \n", np.transpose(b, (2, 0, 1)))    # shape = (3, 2, 4)
'''b.T = 
 [[[ 0  3  6  9]
  [12 15 18 21]]

 [[ 1  4  7 10]
  [13 16 19 22]]

 [[ 2  5  8 11]
  [14 17 20 23]]]'''

# 대각원소와 대각합
a = np.arange(1, 10).reshape(3, 3)
print("a = \n", a)
'''a = 
 [[1 2 3]
 [4 5 6]
 [7 8 9]]'''
b = np.diag(a)    # 대각선 요소 반환
print("b = ", b)    # b =  [1 5 9]

c = np.trace(a)   # 대각선 요소의 합
print(c)   # 15

# 최대 / 최소 위치 구하기
a = np.random.random((3, 4))    # 균등분포
print("a = \n", a)
'''a = 
 [[0.49098882 0.36127393 0.62123288 0.32109887]
 [0.44985657 0.5700598  0.33611477 0.18419704]
 [0.42206885 0.68362122 0.1962283  0.74791646]]'''

print(f'argmax = {np.argmax(a)}')    # 8
print(f'argmax (axis 0 direction) = {np.argmax(a, axis=0)}')    # argmax (axis 0 direction) = [0 2 0 2]
print(f'argmin (axis 0 direction) = {np.argmin(a, axis=0)}')    # argmin (axis 0 direction) = [2 0 2 1]
print(f'argmax (axis 1 direction) = {np.argmax(a, axis=1)}')    # argmax (axis 1 direction) = [2 1 3]
print(f'argmin (axis 1 direction) = {np.argmin(a, axis=1)}')    # argmin (axis 1 direction) = [3 3 2]

# 역행렬과 행렬식
a = np.array([[1, 2, 3],
              [5, 7, 11],
              [21, 29, 31]])
print("a = \n", a)
'''a = 
 [[ 1  2  3]
 [ 5  7 11]
 [21 29 31]]'''
b = np.linalg.inv(a)    # 역행렬
print("b = \n", b)
'''b = 
 [[-2.31818182  0.56818182  0.02272727]
 [ 1.72727273 -0.72727273  0.09090909]
 [-0.04545455  0.29545455 -0.06818182]]'''
c = np.linalg.det(a)    # 행렬식
print(c)    #43.99999999999999

# eigen vecter, eigen value
a = np.array([[4, 2],
              [3, 5]])
print("a = \n", a)
'''a = 
 [[4 2]
 [3 5]]'''

eigenvalues, eigenvectors = np.linalg.eig(a)
print(f'eigenvalues = {eigenvalues}')    # eigenvalues = [2. 7.]
print(f'eigenvextors =\n{eigenvectors}')
'''eigenvextors =
[[-0.70710678 -0.5547002 ]
 [ 0.70710678 -0.83205029]]'''