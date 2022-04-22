a = True
b = False

print(type(a))  #자료형이 bool형으로 지정
print(type(b))  #자료형이 bool형으로 지정

#예시
ex = ['a', 'b', 'c', 'd']
while ex:
    print(ex.pop()) # 마지막 요소부터 ex가 False때까지 하나씩 반환

# bool 연산
print(bool('YouNeedPython'))   # True
print(bool([]))                # False
print(bool((1, 2, 3)))         # True
print(bool({}))                # False
print(bool(0))                 # False
print(bool(1))                 # True