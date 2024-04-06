tmp = list(map(int, input().split()))
a, b = tmp[0], tmp[1]

if a > b:
    print(a * b)
else:
    print(b // a)