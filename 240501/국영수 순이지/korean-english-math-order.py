class Student:
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

students = []
for _ in range(int(input())):
    n, k, e, m = input().split()
    students.append(Student(n, int(k), int(e), int(m)))

students.sort(key=lambda st: (st.kor, st.eng, st.math), reverse=True)

for student in students:
    print(student.name, student.kor, student.eng, student.math)