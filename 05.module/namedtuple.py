from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(11, 22)
print(p)    # Point(x=11, y=22)
print(p.x + p.y)    # 33
print(p[0] + p[1])    # 33
x, y = p
print(x, y)    # 11 22
