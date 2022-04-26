# 파일 열기 모드
# r: 읽기 모드
# w: 쓰기 모드
# a: 추가 모드

# 쓰기 모드 연습
f = open("새파일.txt", 'w')    # 쓰기 모드로 파일 객체 생성
for i in range(1, 11):
    data = "%d번째 테스트입니다.\n" % i
    f.write(data)   # data의 내용을 파일 객체에 쓰기
f.close()   # 파일 객체를 닫아 주는 역할

# 읽기 모드 연습
f = open("새파일.txt", 'r')
while True:
    line = f.readline()      # readline은 파일의 첫번째 줄을 읽어서 변수에 대입
    if line:
        print(line)
    else:
        break;
f.close()

f = open("새파일.txt", 'r')
lines = f.readlines()    # readlines는 파일의 모든 줄은 받아서 리스트 형태로 만들어서 변수에 대입
print(lines)
f.close()

f = open("새파일.txt", 'r')
data = f.read()     # 텍스트 파일의 내용 전체를 그대로 문자열로 돌려줌
print(data)
f.close()

# 추가 모드 연습
f = open("새파일.txt", 'a')    # 기존 내용에 추가적으로 작성
for i in range(11, 21):
    data = "%d번째 테스트입니다.\n" % i
    f.write(data)
f.close()

