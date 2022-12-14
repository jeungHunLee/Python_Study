import pandas as pd
import numpy as np

# 1차원 Series 객체 생성
obj = pd.Series([3, 6, -7, 2])
print(obj)
'''
0    3
1    6
2   -7
3    2
dtype: int64
'''

s = pd.Series([1, 3, 5, np.nan, 6, 8])    # nan: not a number
print(s)    # 요소에 nan이 포함되면 나머지 요소 float 타입
print(s.index)    # RangeIndex(start=0, stop=6, step=1)
print(s.dtype)    # float64
'''
0    1.0
1    3.0
2    5.0
3    NaN
4    6.0
5    8.0
dtype: float64
'''

# Series index 변경
obj = pd.Series([3, 6, -7, 2], index=['a', 'b', 'c', 'd'])    # 기존의 숫자 index도 동일하게 사용가능
print(obj)
'''
a    3
b    6
c   -7
d    2
dtype: int64
'''

# Series data 추가
obj['e'] = 50
print(obj)
'''
a     3
b     6
c    -7
d     2
e    50
dtype: int64
'''

# Series data 삭제(1)
del obj['b']
print(obj)
'''
a     3
c    -7
d     2
e    50
dtype: int64
'''

# Series data 삭제(2)
obj = obj.drop('c')    # obj.drop('c' inplace=Trie) 배열 자가수정
print(obj)
'''
a     3
d     2
e    50
dtype: int64
'''

# Series 객체 생성 (by dic)
obj = pd.Series({'Kim': 32_000,    # 숫자 자리수 구분하기 위한 under bar(_)
                 'Lee': 7_000,
                 'Park': 12_000,
                 'Choi': 14_000})
print(obj)
'''
Kim     32000
Lee      7000
Park    12000
Choi    14000
dtype: int64
'''

# Series name, index nam
obj = pd.Series([3, 6, -7, 2])
obj.name = 'Test data'
obj.index.name = 'No.'
print(obj)
'''
No.
0    3
1    6
2   -7
3    2
Name: Test data, dtype: int64
'''

# Series indexing
a = pd.Series([926, 924, 921, 943, 923])
print(a[0])    # 926
print(a[1])    # 924

# Series operation (by index)
mine = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
yours = pd.Series([100, 300, 200], index=['b', 'a', 'c'])
merge = mine + yours    # 같은 index data끼리 연산
print(merge)
'''
a    310
b    120
c    230
dtype: int64
'''