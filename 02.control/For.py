# for문을 이용한 구구단
for i in range(2, 10):
    for j in range(1, 10):
        print("%d X %d = %d " % (i, j, i * j), end = " ")
        # print 함수는 개행이 포함 되어 있음
        # end는 개행 하지 않고 같은 줄에 출력 하기 위함
    print(" ")

# 리스트 내포를 사용한 구구단
result = [i*j for i in range(2, 10) for j in range(1, 10)]
print(result)
