# indexing, slicing
import numpy as np

a = np.arange(20).reshape(5, 4)
print(a)
'''[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]
 [12 13 14 15]
 [16 17 18 19]]'''
print(f'a[2, 3] = {a[2, 3]}')        # a[2, 3] = 11
print(f'a[0:5, 1] = {a[0:5, 1]}')    # a[0:5, 1] = [ 1  5  9 13 17]
print(f'a[:, 1] = {a[:, 1]}')        # a[:, 1] = [ 1  5  9 13 17]
print(f'a[1:3, :] = \n {a[1:3, :]}')
'''a[1:3, :] = 
 [[ 4  5  6  7]
 [ 8  9 10 11]]'''
print(f'a[-1] = {a[-1]}')          # a[-1] = [16 17 18 19]
print(f'a[:, -1] = {a[:, -1]}')    # a[:, -1] = [ 3  7 11 15 19]
print(a[(0, 2, 3), 2])             # [ 2 10 14]

rows = np.array([True, False, True, True, False])
b = a[rows, :]    # rows가 True인 행에 대하여 slicing
print(b)
'''[[ 0  1  2  3]
 [ 8  9 10 11]
 [12 13 14 15]]'''
