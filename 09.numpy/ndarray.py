# numpy
import numpy as np

# ndarray_test
a = np.arange(15)
print(a)    # [0 1 2 3 4 5 6 7 8 9 10 11 12 13 14]
a = a.reshape(3, 5)    # 3행 5열로 변환
print(a)
'''[[ 0  1  2  3  4]
    [ 5  6  7  8  9]
    [10 11 12 13 14]]'''

print(f'shape = {a.shape}')          # shape = (3, 5)
print(f'ndim= {a.ndim}')             # ndim= 2
print(f'datatype = {a.dtype}')       # datatype = int64
print(f'itemsize = {a.itemsize}')    # itemsize = 8
print(f'size = {a.size}')            # size = 15

# ndarray_declaration
a = np.array([1, 2, 3, 4, 5])    # 인수로 n차원 list 전달
b = np.array([[1, 2, 3],
              [4, 5, 6]])

a = np.arange(5)
b = np.arange(10, dtype=float)    # 크기가 10이고 데이터 타입이 np.float형인 ndarray 객체 생성
c = np.arange(3.1, 5, 0.25)          # start = 3.1, end = 5 step = 0.25

print(a)    # [0 1 2 3 4]
print(b)    # [0. 1. 2. 3. 4. 5. 6. 7. 8. 9.]
print(c)    # [3.1  3.35 3.6  3.85 4.1  4.35 4.6  4.85]

a = np.linspace(0, 0.2, 6)    # [0, 0.2] 사이의 개수가 6개인 ndarray 객체 생성(step은 자동)
print(a)    # [0.   0.04 0.08 0.12 0.16 0.2 ]

a = np.empty((2, 3))    # shape에 해당하는 랜덤 값으로 초기화된 ndarray 객체 생성
print(a)
'''[[0.   0.04 0.08]
 [0.12 0.16 0.2 ]]'''

a = np.ones((2, 3), dtype=np.int64)    # shape에 해당하는 1로 초기화된 ndarray 객체 생성
print(a)
'''[[1 1 1]
 [1 1 1]]'''

a = np.zeros((2, 3))    # shape에 해당하는 0으로 초기화된 ndarray 객체 생성
print(a)
'''[[0. 0. 0.]
 [0. 0. 0.]]'''

d = np.full((2, 3), np.pi)    # shape에 해당하는 value 값으로 초기화된 ndarray 객체 생성
print(d)
'''[[3.14159265 3.14159265 3.14159265]
 [3.14159265 3.14159265 3.14159265]]
'''

a = np.random.randint(10)    # [start, end) 사이의 정수 중 난수 2개 생성
print(a)    # 9

a = np.random.rand(5)    # 균등분포 [0, 1) 사이에서 난수 발생
print(a)    # [0.48924482 0.89698554 0.5453779  0.36352474 0.25115843]

a = np.random.rand(2, 3)
print(a)
'''[[0.6703914  0.80534954 0.02054699]
 [0.53182123 0.91663669 0.53407289]]'''

a = np.random.randn(2, 3)    # 가우시안 정규분포를 따르는 난수 발생
print(a)
'''[[-0.10269388 -1.57915922  1.58780572]
 [ 1.52710981 -1.99334894  0.03991522]]'''