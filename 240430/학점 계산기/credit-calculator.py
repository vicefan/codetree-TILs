n = int(input())
grade = list(map(float, input().split()))
av_grade = sum(grade) / n

print(f"{av_grade:.1f}")

if av_grade >= 4.0:
    print("Perfect")
elif av_grade >= 3.0:
    print("Good")
else:
    print("Poor")