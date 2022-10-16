# abs 함수
print(abs(-5))  # 5
print(abs(1))  # 1

# all 함수
print(all([1, 2, 3]))  # True
print(all([1, 3, 5, 0]))  # False

# any 함수
print(any([1, 2, 3, 0]))  # false

# chr 함수
print(chr(97))  # a
print(chr(64))  # @

# divmod 함수
print(divmod(5, 3))  # (1, 2)

# enumerate 함수
e = enumerate(['You', 'need', 'Python'])
for i in range(3):
    print(next(e))    # tuple 형태로 제공
'''(0, 'You')
(1, 'need')
(2, 'Python')'''

# eval 함수
print(eval('5+5'))  # 10
print(eval('divmod(4, 3)'))  # (1, 1)
print(eval("'hello' + 'world'"))  # helloworld


# filter 함수
def postive(x):
    return x > 0


print(list(filter(postive, [1, -1, 2, -3, -5, 3])))  # [1, 2, 3]

# id 함수
a = 3
print(id(3))  # 4378100016
print(id(a))  # 4378100016


# isinstance 함수
class Test:
    pass


a = Test()
b = 1
print(isinstance(a, Test))  # True
print(isinstance(b, Test))  # False

# len 함수
print(len('Python'))  # 5
print(len([1, 2, 3, 4, 5]))  # 6

# list 함수
print(list('Python'))  # ['P', 'y', 't', 'h', 'o', 'n']
print(list((1, 2, 3)))  # [1, 2, 3]

# max 함수
print(max([1, 3, 5, 7, 9]))     # 9

# min 함수
print(min([1, 3, 5, 7, 9]))     # 1

# pow 함수
print(pow(4, 2))    # 16
print(pow(3, 3))    # 27

# range 함수
print(list(range(5)))           # [0, 1, 2, 3, 4]
print(list(range(1, 5)))        # [1, 2, 3, 4]
print(list(range(1, 10, 2)))    # [1, 3, 5, 7, 9]

# round 함수
print(round(4.2))           # 4
print(round(3.8))           # 4
print(round(3.141592, 2))   # 3.14

# sorted 함수
print(sorted([5, 2, 1, 6, 7]))      # [1, 2, 5, 6, 7]
print(sorted("python"))             # ['h', 'n', 'o', 'p', 't', 'y']

# str 함수
print(str(3))   # '3'

# sum 함수
print(sum([1, 2, 3, 4, 5]))     # 15
print(sum((1, 2, 3)))           # 6

# tuple 함수
print(tuple([1, 2, 3]))     # (1, 2, 3)
print(tuple('python'))      # ('p', 'y', 't', 'h', 'o', 'n')

# zip 함수
print(list(zip([1, 2, 3], [4, 5, 6])))  # [(1, 4), (2, 5), (3, 6)]
print(list(zip("abc", "def")))          # [('a', 'd'), ('b', 'e'), ('c', 'f')]
