from collections import deque

q = deque()
for i in range(1, 6):
    q.append(i)

print(q)    # deque([1, 2, 3, 4, 5])

a = q.popleft()    # 1
b = q.pop()    # 5
print(q)    # deque([2, 3, 4])

# 환형 큐
q.rotate(1)    # 오른쪽으로 회전
print(q)    # deque([4, 2, 3])
q.rotate(-1)    # 왼쪽으로 회전
print(q)    # deque([2, 3, 4])