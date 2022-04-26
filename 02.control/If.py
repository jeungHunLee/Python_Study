# 비교 연산자를 사용한 if문
mathScore = 70
if mathScore >= 50:  # if 조건문은 참과 거짓을 판단
    print("수학 점수가 평균 이상입니다.")

else:
    print("수학 점수가 평균 이하입니다.")

# and, or, not 연산자를 사용한 if문
mathScore = 70
engScore = 50
if mathScore >= 70 and engScore >= 60:  # 둘 다 참인 경우에만 참
    print("합격입니다.")
else:
    print("불합격입니다.")

if mathScore >= 70 or engScore >= 60:   # 둘 중 하나만 참이면 참
    print("합격입니다.");
else:
    print("불합격입니다.")

# x in s, not in s를 이용한 if문
# 'math'과목을 필수로 수강해야 하는 경우
subject = ['math', 'science', 'english', 'history']
if 'math' in subject:
    print("필수 과목을 수강 하였습니다.")
else:
    print("필수 과목을 수강하지 않았습니다.")

# esif문
# 필수 과목으로 'math'나 'science'중 하나를 수강하는 경우
subject = ['science', 'english', 'history', 'athletic']
if 'math' in subject:
    print("필수 과목을 수강 하였습니다.")
elif 'science' in subject:
    print("필수 과목을 수강 하였습니다.")
else:
    print("필수 과목을 수강하지 않았습니다.")

# 조건부 표현식
score = 75
message = "pass" if score >= 70 else "nonpass"
print(message)
