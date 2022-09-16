# 가변 변수를 가지는 print문
# sep은 iterable한 객체를 출력할때 그 사이사이에 문자열을 삽입
print("철수", "영희", "바둑이", sep='<->')    # 철수<->영희<->바둑이

# 입력받은 문자열을 정수형 혹은 실수형으로 변환
# eval 함수: 입력 받은 문자열이 int형이면 int형으로 String형이면 String형으로 자동 형 변환
num1 = eval(input())    # 10
num2 = eval(input())    # 1.1

print(type(num1))    # <class 'int'>
print(type(num2))    # <class 'float'>
