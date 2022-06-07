import heapq

# heappush 메서드 구현
numbers = [3, 8, 5, 9, 7]
result = []
for i in numbers:
    heapq.heappush(result, i)
print(result)   # [3, 7, 5, 9, 8]

# heappop 메서드 구현
for _ in range(len(numbers)):
    print(heapq.heappop(result))    # 3 5 7 8 9

# heapify 메서드 구현
numbers = [3, 8, 5, 9, 7]
heapq.heapify(numbers)
print(numbers)  # [3, 7, 5, 9, 8]

