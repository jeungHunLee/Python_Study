# while 반복문
# 입장객이 10명 이후에는 입장을 제한하기
personCount = 0
while personCount < 10:
    personCount += 1    # python에는 증감연산자(++, -- 등)이 없음
    print("입장객의 수는 %d명입니다." % personCount)
    if personCount == 10:
        print("입장을 제한합니다.")

# 1부터 20까지의 수 중 3의 배수와 5의 배수 제외하기
num = 0
while True:
    num += 1
    if num == 21:
        break   # num이 21일때 while문을 빠져나감
    elif num % 3 == 0 or num % 5 == 0:
        continue    # 다시 12번째 줄로 돌아감
    else:
        print(num)