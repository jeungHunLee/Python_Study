# closure
def outer(num):
    def inner():
        print(num)
    return inner

f1 = outer(3)
f2 = outer(10)
f1()    # 3
f2()    # 10

# decolator
def trace(func):
    def wrapper():
        print('함수 시작')
        func()
        print('함수 끝')
    return wrapper

@trace
def hello():
    print("hello")

hello()
'''함수 시작
hello
함수 끝'''