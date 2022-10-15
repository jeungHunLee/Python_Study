# broadcasting
import numpy as np

a = np.arange(3)
b = a + 5    # [1 2 3] + [5 5 5]
print(b)    # [5 6 7]

a = np.arange(9, dtype=float).reshape(3, 3)
b = np.arange(1, 4, dtype=float)
print(a + b)
'''[[ 1.  3.  5.]
 [ 4.  6.  8.]
 [ 7.  9. 11.]]'''

a = np.arange(3).reshape(3, 1)
b = np.arange(3)
print(a + b)
'''[[0 1 2]
 [1 2 3]
 [2 3 4]]'''

a = np.arange(24).reshape(3, 4, 2)
b = np.arange(8).reshape(4, 2)
print(a + b)
'''
[[[ 0  2]
  [ 4  6]
  [ 8 10]
  [12 14]]

 [[ 8 10]
  [12 14]
  [16 18]
  [20 22]]

 [[16 18]
  [20 22]
  [24 26]
  [28 30]]]'''
