# Python 함수의 형태
def add(a, b):
    return a + b
print(add(5, 6))

# 입력값이 없는 함수
def hi():
    return "Hello"
print(hi())

# 결과값이 없는 함수
def mul(a, b):
    print("%d X %d = %d" %(a, b, a * b))
    # 결과값은 오직 return 명령으로만 반환
print(mul(3, 4))

# 더하기와 곱하기 함수
def add_mul(choice, *args):     # *args는 입력값을 받아서 tuple 형태로 만들어줌
    if choice == "add":
        result = 0
        for i in args:
            result += i
        return result
    elif choice == "mul":
        result = 1
        for i in args:
            result *= i
        return result
print(add_mul("add", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

# 매개변수 초깃값 설정
def intro_myself(name, old, man = True):    # 초기값을 설정해야 되는 매개변수는 마지막에 위치
    print("나의 이름은 %s입니다." % name)
    print("나의 나이는 %d살 입니다." % old)
    if man:
        print("저는 남자입니다.")
    else:
        print("저는 여자입니다.")
intro_myself("이정훈", 24)

# 변수의 영향력 범위
a = 1
def vartest():
    global a    # 함수 외부의 전역 변수 a를 직접 이용
    a += 1
vartest()
print(a)

# lamda식
mul = lambda a, b: a * b
result = mul(3, 7)
print(result)