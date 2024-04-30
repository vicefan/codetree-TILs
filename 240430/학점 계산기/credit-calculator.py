n = int(input())
grade = list(map(float, input().split()))
av_grade = sum(grade) / n

print(round(sum(grade) / n, 1))

if av_grade >= 4:
    print("Perfect")
elif av_grade >= 3:
    print("Good")
else:
    print(Poor)