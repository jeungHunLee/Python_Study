from collections import OrderedDict
d = OrderedDict()
d[1] = 'one'
d[2] = 'two'
d[3] = 'three'
d[4] = 'four'
d[5] = 'five'

print(d)    # OrderedDict([(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five')])
D = sorted(d.items(), key=lambda x: x[1])
print(D)    # [(5, 'five'), (4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]

d = OrderedDict(lambda : 0)   # 기본값 0으로 초기화