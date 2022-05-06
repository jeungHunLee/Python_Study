import Calculator

print(Calculator.add(5, 2))
print(Calculator.sub(5, 1))
print(Calculator.mul(2, 4))
print(Calculator.div(6, 4))

# 객체 생성
circleTest = Calculator.Circle(3)   # 반지름의 길이가 3인 원 객체 생성

print(circleTest.extent())  # 원의 넓이
print(circleTest.round())  # 원의 둘레
