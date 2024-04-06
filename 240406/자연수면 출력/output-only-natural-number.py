tmp = list(map(int, input().split()))
a, b = tuple(tmp)

if a > 0:
    print(str(a) * b)
else:
    print(0)