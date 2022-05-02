import Student

# 객체 생성
studentLee = Student.Student("Lee", 24, 76, 85)

studentLee.showInfo()
studentLee.sum()
studentLee.mathGrade()
studentLee.engGrade()
print()

# 객체 생성
studentKim = Student.ModStudent("Kim", 25, 84, 70)

studentKim.showInfo()
studentKim.sum()
studentKim.average()
studentKim.mathGrade()
studentKim.engGrade()
