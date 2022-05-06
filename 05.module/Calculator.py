PI = 3.141592


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


class Circle:
    def __init__(self, r):  # 생성자
        self.r = r

    def extent(self):  # 원의 넓이 반환하는 메서드
        return (self.r ** 2) * PI

    def round(self):  # 원의 둘레 반환하는 메서드
        return 2 * PI * self.r
