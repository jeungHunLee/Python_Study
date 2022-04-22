# 집합 자료형 생성
s1 = set("Good")
s2 = set([1, 2, 3])
print(s1)
print(s2)

# 집합 자료형의 특징
# 반환값에 중복을 허용하지 않음
# 순서가 없음(집합 자료형에 접근 하기 위해서는 리스트나 튜플로 변환 해야함)

# 교집합
s1 = set([1, 2, 3, 4, 5])
s2 = set([3, 4, 5, 6, 7])
print(s1 & s2)  # s1.intersection(s2)

# 합집합
print(s1 | s2)  # s1.union(s2)

# 차집합
print(s1 - s2)  # s1.difference(s2)
print(s2 - s1)  # s2.difference(s1)

# 1개의 값 추가하기(add)
s1 = set([1, 2, 3])
s1.add(4)   # 오직 1개의 값만을 추가 가능
print(s1)

# 여러개의 값 추가하기(update)
s1 = set([1, 2, 3])
s1.update([4, 5])
print(s1)

# 값 제거하기(remove)
s1 = set([1, 2, 3, 4, 5])
s1.remove(3)
print(s1)