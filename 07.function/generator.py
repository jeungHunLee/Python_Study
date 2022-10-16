# generator(iterator 객체를 만들어 주는 함수)
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for x in countdown(10):
    print(x, end=' ')    # 10 9 8 7 6 5 4 3 2 1
print()

def generator(arr):
    yield from arr    # sequence 객체에서 요소를 순서대로 반환

g = generator([1, 2, 3, 4])    # generator 객체 생성
print(list(g))    # [1, 2, 3, 4]