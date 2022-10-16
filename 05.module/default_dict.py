from collections import defaultdict

d = defaultdict(lambda: 0)    # default 값 0 반환
d['first']    # key 추가
d['second']
print(d['first'])    # 0
print(d['second'])    # 0

s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)    # default 값으로 빈 list 반환
for k, v in s:
    d[k].append(v)

print(sorted(d.items(), key=lambda x: x[0]))    # [('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]
