tmp = list(map(int, input().split()))

a, b = tuple(tmp)
for i in range(a, b + 1, 2):
    print(i, end=' ')