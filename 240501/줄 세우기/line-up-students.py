class Student:
    def __init__(self, h, w, number):
        self.h = h
        self.w = w
        self.number = number

sts = []

for i in range(int(input())):
    h, w = map(int, input().split())
    sts.append(Student(h, w, i + 1))

sts.sort(key=lambda s:(-s.h, -s.w, s.number))

for s in sts:
    print(s.h, s.w, s.number)