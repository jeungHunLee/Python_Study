# 사용자 입력
age = (int)(input("나이를 입력하세요: "))   # input에서 받는 디폴트값은 String형
if age >= 20:
    print("성인입니다.")
elif age >= 17:
    print("고등학생입니다.")
elif age >= 14:
    print("중학생입니다.")
elif age >= 8:
    print("초등학생입니다.")
else:
    print("미취학 아동입니다.")

# print문
# print문에서 큰따옴표로 둘러싸인 문자열은 문자열의 합과 같다.
print("You" "need" "Python")    # "You"+"need"+"Python" 과 같음

# 문자열의 띄어쓰기는 콤마(,)로 한다.
print("You", "need", "Python")

