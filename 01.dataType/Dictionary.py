# 딕셔너리 쌍 추가
a = {1: 'a'}
a[2] = 'b'
a[3] = ['c', 'd']
print(a)

# 딕셔너리 요소 삭제
a = {1: 'a', 2: 'b'}    # Key가 1인 요소 삭제
del a[1]
print(a)

# Key를 이용하여 value 얻기
dic = {'phone': 'iphone', 'laptop': 'macbook', 'music': 'airpods'}
print(dic['phone']) # value 값인 'iphone' 출력

# 중복되는 Key 값이 있으면 하나 제외 나머지는 무시된다.
# Key값에 리스트형은 불가능하다.(변수 불가능)

# 딕셔너리 Key 리스트 만들기(keys)
dic1 = {'phone': 'iphone', 'laptop': 'macbook', 'music': 'airpods'}
print(dic1.keys())  # dic1_keys() 객체 반환

for i in dic1.keys():   # dic1_keys() 객체의 리스트 요소 출력하기
    print(i)

# 딕셔너리 Value 리스트 만들기(values)
dic1 = {'phone': 'iphone', 'laptop': 'macbook', 'music': 'airpods'}
print(dic1.values())    # dic1_value() 객체 반환

# Key, Value 쌍 얻기(item)
dic1 = {'phone': 'iphone', 'laptop': 'macbook', 'music': 'airpods'}
print(dic1.items()) #dic1_items 객체 반환

# Key: Value 쌍 제거(clear)
a = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
a.clear()
print(a)

# Key로 Value 얻기(get)
a = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
print(a.get(1))
print(a.get(5)) # 존재하지 않는 Key값으로 None 반환
# print(a[5]) ->  존재하지 않는 Key값으로 오류 발생

# 딕셔너리 안에 Key가 존재 하는지 확인
a = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
print(1 in a)   #존재하면 True 반환
print(5 in a)   #존재하지 않으면 False 반환
