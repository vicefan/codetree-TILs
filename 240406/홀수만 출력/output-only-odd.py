tmp = list(map(int, input().split()))
a, b = tuple(tmp)

for i in range(a, b + 1):
    if i % 2 == 1:
        print(i, end=' ')