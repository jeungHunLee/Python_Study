# 문자열 더하기
a = "Life is short"
b = " You need Python"

print(a + b)

# 문자열 곱하기
a = "Python"

print(a * 2)

# 문자열 길이 구하기 len
a = "\"Life is too short, You need Python\", he said"
# 문자 앞 '\'는 문자 자체를 말함

print(len(a))

# 문자열 인덱싱
a = "Life is too short, You need Python"

print(a[2])
print(a[-1])  # 문자열 a에서 뒤에서 첫번째 문자 출력

b = a[0] + a[1] + a[2] + a[3]
print(b)
print(a[0:4])  # 문자열 a에서 0번부터 3번까지 문자 슬라이싱
print(a[19:])  # 문자열 a에서 19번째부터 끝까지 출력
print(a[:])  # 문자열 a를 처음부터 끝까지 출력

# 문자열 formating
print("I have %d apple device." % 3)
print("I have %s apple device." % "three")

number = 3
print("I have %d apple device" % number)

a = 3
b = "china"
print("I have %s apple device, They were made in %s" % (a, b))
# %s는 자동으로 %뒤에 값을 문자열로 바꿈

# 정렬과 공백
print("%10s" % "hi")  # 길이 10으로 문자를 오른쪽 정렬 하고 나머지는 공백
print("%-10s" % "hi")  # 길이 10으로 문자를 왼쪽 정렬 하고 나머지는 공백

# 소수점 표현
print("%0.4f" % 3.141592)  # 소수점 아래 네자리까지 출력
print("%10.4f" % 3.141592) # 길이 10으로 소수점 아래 네자리까지 출력

# format 함수를 사용한 formating
print("I have {0} apple device".format(3))
print("I have {0} apple device".format("three"))

number = 3
print("I have {0} apple device".format(number))

print("I have {0} apple device, There ware made in {country}".format(3, country="china"))
# non-keyword arg가 앞에  keyword arg가 뒤에 위치(반대의 경우 에러)

print("{0:<10}".format("python"))  # 왼쪽 정렬
print("{0:>10}".format("python"))  # 오른쪽 정렬
print("{0:^10}".format("python"))  # 중앙 정렬
print("{0:!^10}".format("python"))  # 정렬 문자(<,>,^) 앞에 문자를 넣어 공백을 채움

a = 3.141592
print("{0:0.4f}".format(a))
print("{0:10.4f}".format(a))

# 문자 개수 세기(count)
a = "mycomputer"
print(a.count('m'))

# 위치 알려주기(find)
a = "Life is too short, You need Python"
print(a.find('n'))  # 존재 하지 않는 문자는 -1을 반환

# 위치 알려주기(index)
a = "Life is too short, You need Python"
print(a.index('n'))  # 존재 하지 않는 문자는 오류 발생

# 문자열 삽입(join)
print(",".join("ABCD"))

# 소문자를 대문자로 바꾸기(upper)
a = "python"
print(a.upper())

# 대문자를 소문자로 바꾸기(lower)
a = "PYTHON"
print(a.lower())

# 왼쪽 공백 지우기(lstrip)
a = " hi"
print(a.lstrip())

# 오르쪽 공백 지우기(rstrtip)
a = "hi "
print(a.rstrip())

# 양쪽 공백 지우기(strip)
a = " hi "
print(a.strip)

#문자열 바꾸기(replace)
a = "You need Python"
print(a.replace('You', 'I'))

# 문자열 나누기(split)
a = "You need Python"
print(a.split()) # 공백 기준으로 문자열 나누기
b = "a:b:c:d"
print(b.split(':'))  # ':'기준으로 문자열 나누기