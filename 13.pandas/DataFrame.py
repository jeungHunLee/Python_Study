import numpy as np
import pandas as pd

# Dataframe 생성 (by dic)
data = {'Apples': [3, 2, 0, 1],
        'Oranges': [0, 3, 7, 2]}
df = pd.DataFrame(data)
print(df)
'''
   Apples  Oranges
0       3        0
1       2        3
2       0        7
3       1        2
'''

# 시계열 데이터 생성
dndx1 = pd.date_range(start='1/1/2020', end='1/08/2020')
print(dndx1)
'''
DatetimeIndex(['2020-01-01', '2020-01-02', '2020-01-03', '2020-01-04',
               '2020-01-05', '2020-01-06', '2020-01-07', '2020-01-08'],
              dtype='datetime64[ns]', freq='D')
'''
dndx2 = pd.date_range(start='20200301', periods=3)    # periods: 개수
print(dndx2)
'''DatetimeIndex(['2020-03-01', '2020-03-02', '2020-03-03'], dtype='datetime64[ns]', freq='D')'''
dndx3 = pd.date_range(start='20200101', periods=3, freq='2H20min')    # freq: 2 hour 30 minutes
print(dndx3)
'''
DatetimeIndex(['2020-10-01 00:00:00', '2020-10-01 02:20:00',
               '2020-10-01 04:40:00'],
              dtype='datetime64[ns]', freq='140T')
'''
dndx4 = pd.date_range(start='1/20/2020', periods=4, freq='2M')    # freq: 2 month end
print(dndx4)
'''DatetimeIndex(['2020-01-31', '2020-03-31', '2020-05-31', '2020-07-31'], dtype='datetime64[ns]', freq='2M')'''

# Timestamp
ts1 = pd.Timestamp(2020, 1, 1, 10)
print(ts1)    # 2020-01-01 10:00:00
ts2 = pd.Timestamp('20200101T0920')
print(ts2)    # 2020-01-01 09:20:00
ts3 = pd.Timestamp(year=2020, month=1, day=1, hour=12)
print(ts3)    # 2020-01-01 12:00:00
ts4 = pd.Timestamp(year=2020, month=1, day=1)
print(ts4)    # 2020-01-01 00:00:00

# DataFrame 생성 (by list)
dates = pd.date_range('20180521', periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
print(df)
'''
                   A         B         C         D
2018-05-21 -0.534362  0.351817  2.427218 -0.068412
2018-05-22  1.527308  1.776466  0.491654 -1.523790
2018-05-23 -0.891339  0.433528  0.200155  0.537185
2018-05-24 -0.771942 -0.498719  0.206691 -0.474455
2018-05-25  0.879848 -0.621205  0.373636 -1.209847
2018-05-26 -0.733235  0.209051  0.472730  1.162827
'''

# Categorical
df = pd.DataFrame({'A': 1.0,
                   'B': pd.Timestamp('20180521'),
                   'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                   'D': np.array([3] * 4, dtype='int32'),
                   'E': pd.Categorical(['test', 'train', 'test', 'train']),    # Categorical 객체
                   'F': 'foo'})
print(df)
'''
     A          B    C  D      E    F
0  1.0 2018-05-21  1.0  3  test  foo
1  1.0 2018-05-21  1.0  3  train  foo
2  1.0 2018-05-21  1.0  3   test  foo
3  1.0 2018-05-21  1.0  3  train  foo
'''

# DataFrame 속성
data = {'Name': ['Lee', 'Lee', 'Choi', 'Kim', 'Park'],
        'Year': [2013, 2014, 2015, 2016, 2015],
        'Points': [1.5, 1.8, 3.6, 2.4, 2.9]}
df = pd.DataFrame(data)
print(df.index)    # RangeIndex(start=0, stop=5, step=1)
print(df.columns)    # Index(['Name', 'Year', 'Points'], dtype='object')
print(df.values)
'''
[['Lee' 2013 1.5]
 ['Lee' 2014 1.8]
 ['Choi' 2015 3.6]
 ['Kim' 2016 2.4]
 ['Park' 2015 2.9]]
 '''

# DataFrame index 변경
data = {'Name': ['Lee', 'Lee', 'Choi', 'Kim', 'Park'],
        'Year': [2013, 2014, 2015, 2016, 2015],
        'Point': [1.5, 1.8, 3.6, 2.4, 2.9]}
df = pd.DataFrame(data, index=['one', 'two', 'three', 'four', 'five'])    # index 크기가 더 클 경우 나머지 행은 nan
print(df)
'''
       Name  Year  Point
one     Lee  2013    1.5
two     Lee  2014    1.8
three  Choi  2015    3.6
four    Kim  2016    2.4
five   Park  2015    2.9
'''

# DataFrame column 순서 변경
data = {'Name': ['Lee', 'Lee', 'Choi', 'Kim', 'Park'],
        'Year': [2013, 2014, 2015, 2016, 2015],
        'Points': [1.5, 1.8, 3.6, 2.4, 2.9]}
df = pd.DataFrame(data, columns=['Year', 'Name', 'Point', 'Penalty'])    # index 크기가 더 클 경우 나머지 행은 nan
print(df)
'''   Year  Name Point Penalty
0  2013   Lee   NaN     NaN
1  2014   Lee   NaN     NaN
2  2015  Choi   NaN     NaN
3  2016   Kim   NaN     NaN
4  2015  Park   NaN     NaN
'''

# Dataframe index, column name 변경
data = {'Name': ['Lee', 'Lee', 'Choi', 'Kim', 'Park'],
        'Year': [2013, 2014, 2015, 2016, 2015],
        'Points': [1.5, 1.8, 3.6, 2.4, 2.9]}

df = pd.DataFrame(data)
df.index.name = 'No.'
df.columns.name = 'Information'
print(df)
'''
Information  Name  Year  Points
No.                            
0             Lee  2013     1.5
1             Lee  2014     1.8
2            Choi  2015     3.6
3             Kim  2016     2.4
4            Park  2015     2.9
'''

# DataFrame indexing & slicing
data = {'Name': ['Lee', 'Lee', 'Choi', 'Kim', 'Park'],
        'Year': [2013, 2014, 2015, 2016, 2015],
        'Points': [1.5, 1.8, 3.6, 2.4, 2.9]}
df = pd.DataFrame(data)

print(df['Year'], '\n')    # column indexing
'''
0    2013
1    2014
2    2015
3    2016
4    2015
Name: Year, dtype: int64 
'''
print(df[['Name', 'Points']], '\n')
'''
   Name  Points
0   Lee     1.5
1   Lee     1.8
2  Choi     3.6
3   Kim     2.4
4  Park     2.9 
'''
print(df.iloc[1:3])
'''
   Name  Year  Points
1   Lee  2014     1.8
2  Choi  2015     3.6
'''

data = {'open': [11650, 11100, 11200, 11100, 11000],
        'high': [12100, 11800, 11200, 11100, 11150],
        'low': [11600, 11050, 10900, 10950, 10900],
        'close': [11900, 11600, 11000, 11100, 11050]}
data_day = pd.DataFrame(data)
print(data_day, '\n')
'''
    open   high    low  close
0  11650  12100  11600  11900
1  11100  11800  11050  11600
2  11200  11200  10900  11000
3  11100  11100  10950  11100
4  11000  11150  10900  11050 
'''

# column 순서 변경
data_day = pd.DataFrame(data, columns=['close', 'high', 'low', 'open'], index=['16.02.29', '16.02.26', '16.02.25', '16.02.24', '16.02.23'])
print(data_day)
'''
          close   high    low   open
16.02.29  11900  12100  11600  11650
16.02.26   11600  11800  11050  11100
16.02.25  11000  11200  10900  11200
16.02.24  11100  11100  10950  11100
16.02.23  11050  11150  10900  11000
'''

print(data_day.loc['16.02.29'])    # loc label indexing
'''
close    11900
high     12100
low      11600
open     11650
Name: 16.02.29, dtype: int64
'''

print(data_day.iloc[0:3])   # iloc position indexing
'''
          close   high    low   open
16.02.29  11900  12100  11600  11650
16.02.26  11600  11800  11050  11100
16.02.25  11000  11200  10900  11200
'''

print(data_day.iloc[0:3, 0:2])    # rows: 0~2, colums: 0~1
'''
          close   high
16.02.29  11900  12100
16.02.26  11600  11800
16.02.25  11000  11200
'''

print(data_day.iloc[[0, 1, 2], [0, 1]])    # rows: 0~2, columns: 0~1
'''
          close   high
16.02.29  11900  12100
16.02.26  11600  11800
16.02.25  11000  11200
'''

# boolean indexing
dates = pd.date_range('20180521', periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
print(df)
'''
                   A         B         C         D
2018-05-21  1.857864  1.332762 -0.209024  0.200171
2018-05-22 -0.145525  0.847056  0.913299  0.777847
2018-05-23  1.131711 -3.015309  1.379898 -1.114265
2018-05-24 -0.396007  0.147413  0.154416  0.845249
2018-05-25 -0.560304  1.473959 -0.829343  0.777716
2018-05-26 -0.455054  1.361415  0.896933 -0.567381
'''

print(df[df.A > 0])    # A열이 0보다 큰 행 출력
'''
                   A         B         C         D
2018-05-21  0.349109  0.064623 -0.804128  0.828826
2018-05-22  1.354925  0.073021 -0.369742 -0.971345
2018-05-25  0.641588 -0.667090  0.241171  0.103390
'''

print(df[df > 0])    # df 전체에서 0보다 큰 항목만 표시
'''
                   A         B         C   D
2018-05-21  1.934041       NaN       NaN NaN
2018-05-22       NaN  0.558971       NaN NaN
2018-05-23  1.249390       NaN       NaN NaN
2018-05-24  0.474131       NaN  0.376445 NaN
2018-05-25  1.412110  2.448902       NaN NaN
2018-05-26       NaN  0.950866       NaN NaN
'''

print(df > 0)    # 모든 항목이 0보다 큰지 확인
'''
                A      B      C      D
2018-05-21   True   True  False   True
2018-05-22  False   True  False   True
2018-05-23   True   True   True  False
2018-05-24  False  False   True  False
2018-05-25   True   True   True  False
2018-05-26   True   True  False   True
'''

# Deep Copy & Append column
dates = pd.date_range('20180521', periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
print(df)
'''
                   A         B         C         D
2018-05-21  1.697003  0.245877 -0.414813  0.515403
2018-05-22 -1.068003 -0.513253 -1.140229  2.255075
2018-05-23  2.264191  1.003858 -2.116394  1.441611
2018-05-24  0.364636 -0.316648 -0.583468 -0.737703
2018-05-25  0.089920  0.859231 -1.527726 -0.202008
2018-05-26  0.053814 -0.507982  1.377266 -0.436794
'''

df2 = df.copy()    # deep copy
df2['E'] = ['one', 'one', 'two', 'three', 'four', 'three']    # 열 추가
print(df2)
'''
                   A         B         C         D      E
2018-05-21  0.149761 -0.202239 -2.249103  0.026162    one
2018-05-22 -1.312671 -0.073002 -1.819937 -1.373865    one
2018-05-23 -1.864487 -0.733860  0.616643  0.226030    two
2018-05-24  0.203718 -0.547996  0.648440  0.473098  three
2018-05-25 -1.385480 -0.165637  0.784976  1.050049   four
2018-05-26 -1.021520 -0.491580 -0.322240 -0.730722  three
'''

# setting
dates = pd.date_range('20180521', periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
s1 = pd.Series([1, 2, 3, 4, 5, 6], index=dates)
df['F'] = s1    # column 추가
df.at[dates[0], 'A'] = 0    # 행라벨, 열라벨
df.iat[1, 2] = 0    # 행번호, 열번호
df.loc[:, 'D'] = np.array([5] * len(df))
df[df < 0] = -df    # df 전체에서 음수값에 - 곱하기
print(df)
'''
                   A         B         C  D  F
2018-05-21  0.000000  0.755973  0.304128  5  1
2018-05-22  0.409464  0.095894  0.000000  5  2
2018-05-23  1.352553  0.202118  0.179356  5  3
2018-05-24  1.481917  0.767092  1.062492  5  4
2018-05-25  0.490623  0.103656  0.192599  5  5
2018-05-26  1.167549  0.050609  0.025150  5  6
'''

# reindexing
dates = pd.date_range('20180521', periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
df = df.reindex(index=dates[:4], columns=list(df.columns) + ['E'])    # 새로운 객체 반환
df.loc[:dates[1], 'E'] = 1.0
print(df)
'''
                   A         B         C         D    E
2018-05-21  0.382476 -0.006663 -1.244114 -1.148147  1.0
2018-05-22 -1.342168 -1.216456  0.758127 -0.116318  1.0
2018-05-23  0.951171 -0.530992 -1.232678  1.669614  NaN
2018-05-24 -0.255452 -0.618769 -1.301700  0.850652  NaN
'''