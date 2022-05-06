class Student:

    # 생성자
    def __init__(self, name, age, mathScore, engScore):
        self.name = name
        self.age = age
        self.mathScore = mathScore
        self.engScore = engScore

    # 메서드
    def setdata(self, name, age, mathScore, engScore):
        self.name = name
        self.age = age
        self.mathScore = mathScore
        self.engScore = engScore

    def showInfo(self):  # 학생 정보
        print("학생의 이름은 %s이고, 나이는 %d입니다." % (self.name, self.age))

    def sum(self):  # 점수 합계
        result = self.mathScore + self.engScore
        print("점수의 합은 %d입니다." % result)

    def mathGrade(self):  # 수학 점수 등급
        if self.mathScore >= 90:
            print("A학점입니다.")

        elif self.mathScore >= 80:
            print("B학점입니다.")

        elif self.mathScore >= 70:
            print("C학점입니다.")

        elif self.mathScore >= 60:
            print("D학점입니다.")

        else:
            print("F학점입니다.")

    def engGrade(self):  # 영어 점수 등급
        if self.engScore >= 90:
            print("A학점입니다.")

        elif self.engScore >= 80:
            print("B학점입니다.")

        elif self.engScore >= 70:
            print("C학점입니다.")

        elif self.engScore >= 60:
            print("D학점입니다.")

        else:
            print("F학점입니다.")


class ModStudent(Student):  # 클래스 상속
    def average(self):  # 점수 평균 메서드 추가
        result = (self.mathScore + self.engScore) / 2
        print("점수의 평균은 %d입니다." % result)

    def mathGrade(self):  # 메서드 오버라이딩
        if self.mathScore >= 95:
            print("A학점입니다.")

        elif self.mathScore >= 85:
            print("B학점입니다.")

        elif self.mathScore >= 75:
            print("C학점입니다.")

        elif self.mathScore >= 65:
            print("D학점입니다.")

        else:
            print("F학점입니다.")
