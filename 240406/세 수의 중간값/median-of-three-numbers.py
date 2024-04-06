tmp = list(map(int, input().split()))
a, b, c = tuple(tmp)

if b > a and b < c:
    print(1)
else:
    print(0)