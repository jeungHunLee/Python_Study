#리스트 인덱싱
a = [1, 3, 5, ['a', 'b', 'c']]
print(a[0])
print(a[-1]) # 리스트 a의 마지막 요소
print(a[-1][0]) # 리스트 a의 마지막 요소의 첫번째 요소

#리스트 슬라이싱
a = [1, 2, 3, 4, 5]
b = a[:2]  # 처음부터 1번까지
c = a[2:]  # 2번부터 끝까지
print(b)
print(c)

# 리스트 더하기
a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)

# 리스트 반복
a = [1, 2, 3]
print(a * 2)

# 리스트 길이 구하기
a = [1, 2, 3, 4, 5]
print(len(a))

# 정수와 문자열 더하기
a = [1, 2, 3]
print(str(a[1]) + "python")  #str은 정수나 실수를 문자열로 바꿔주는 파이썬 내장 함수

# 리스트에 요소 추가(append)
a = [1, 2, 3]
a.append([4, 5]) # 리스트에 [4, 5]추가
print(a)

# 리스트 정렬(sort)
a = [4, 1, 3, 2]
a.sort()
print(a)

# 리스트 뒤집기(reverse)
a = [4, 1, 3, 2]
a.reverse()  # 현재 리스트 순서 그대로 역순으로 뒤집는다.
print(a)

# 위치 반환(index)
a = [4, 1, 3, 2]
print(a.index(1))  # 리스트에서 '1'의 위치 반환

# 리스트에 요소 삽입(insert)
a = [1, 2, 3, 4]
a.insert(0, 5)  # 0번째 자리에 요소 '5'삽입
print(a)

# 리스트 요소 제거(remove)
a = [1, 2, 3, 4, 3, 3, 1, 2]
a.remove(3) # 리스트에서 첫번째로 나오는 '3'을 제거
print(a)

# 리스트 요소 끄집어 내기(pop)
a = [1, 2, 3, 4]
print(a.pop())  # 리스트의 마지막 요소 출력 후 삭제
print(a.pop(2)) # 리스트의 2번째 요소 출력 후 삭제
print(a)

#리스트 요소 개수 세기(count)
a = [1, 2, 3, 1, 1, 2, 3]
print(a.count(1))

# 리스트 확장(extend)
a = [1, 2, 3]
a.extend([4, 5])
print(a)