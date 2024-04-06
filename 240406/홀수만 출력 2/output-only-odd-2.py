tmp = list(map(int, input().split()))
b, a = tuple(tmp)

for i in range(b, a - 1, -1):
    if i % 2 == 1:
        print(i, end=' ')