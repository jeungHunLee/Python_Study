# 오류 예외 처리
try:
    4 / 0
except ZeroDivisionError as e:
    print(e)

# finally
f = open('test.txt', 'w')
try:
    pass
finally:
    f.close()  # try문의 오류 발생 여부 상관 없이 실행

# 여러개 오류 처리
try:
    a = [1, 2]
    print(a[3])
    4 / 0
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
    # IndexError가 먼저 발생 하여 이후 문장은 실행 되지 않음

except IndexError:
    print("존재하지 않는 인덱스입니다.")

# 오류 회피
try:
    4 / 0
except ZeroDivisionError:
    pass  # 오류가 발생 하더라도 오류 회피


# 오류 강제 발생
class Customer:
    def discount(self, price):
        raise NotImplementedError


class VipCustomer(Customer):
    def discount(self, price):
        price -= (price * 0.1)
        print(price)


person = VipCustomer()
person.discount(12000)
