# Python 함수의 형태
def add(a, b):
    return a + b


print(add(5, 6))  # 11


# 입력값이 없는 함수
def hi():
    return "Hello"


print(hi())  # Hello


# 결과값이 없는 함수
def mul(a, b):
    print("%d X %d = %d" % (a, b, a * b))
    # 결과값은 오직 return 명령으로만 반환


print(mul(3, 4))  # 3 X 4 = 12


# 더하기와 곱하기 함수
def add_mul(choice, *args):  # *args는 입력값을 받아서 tuple 형태로 만들어줌
    if choice == "add":
        result = 0
        for i in args:
            result += i
        return result
    elif choice == "mul":
        result = 1
        for arg in args:
            result *= arg
        return result


print(add_mul("add", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10))  # 55

def sum_many(*args, times):  # *args 뒤에 오는 매개변수는 반드시 키워드 인수
    sum = 0
    for arg in args:
        sum += arg * times

    return sum


print(sum_many(1, 2, 3, times=2))  # 12

# 키워드 가변 매개변수
def print_kwargs(**kwargs):    # 인수를 받아 딕셔너리 형태로 전달
    print(list(kwargs.keys()))
    print(list(kwargs.values()))

print_kwargs(one="하나", two="둘", three="셋")    # ['one', 'two', 'three']
                                                # ['하나', '둘', '셋']

# 키워드 인수
def person(name, age):
    print(f'나의 이름은 {name}이고 나이는 {age}입니다.')


person(name="Lee", age=99)  # 나의 이름은 Lee이고 나이는 99입니다.


# 키워드 인수와 위치 인수 동시에 사용
def add_num(a, *, b, c):  # '*'뒤의 인수는 반드시 키워드 인수로 인식
    return a + b + c


print(add_num(1, b=2, c=3))  # 6


# 매개변수 초깃값 설정(default 인수)
def intro_myself(name, old, man=True):  # 초기값을 설정해야 되는 매개변수는 마지막에 위치
    print("나의 이름은 %s입니다." % name)
    print("나의 나이는 %d살 입니다." % old)
    if man:
        print("저는 남자입니다.")
    else:
        print("저는 여자입니다.")


intro_myself("Lee", 99)  # 나의 이름은 Lee입니다.
                         # 나의 나이는 99살 입니다.
                         # 저는 남자입니다.

# 변수의 영향력 범위
a = 1
def vartest():
    global a  # 함수 외부의 전역 변수 a를 직접 이용
    a += 1

vartest()
print(a)  # 2

# lamda식
mul = lambda a, b: a * b
result = mul(3, 7)
print(result)  # 21
