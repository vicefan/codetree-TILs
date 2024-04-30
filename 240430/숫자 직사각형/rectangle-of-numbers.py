n, m = list(map(int, input().split()))

tmp = 1
for _ in range(n):
    for _ in range(m):
        print(tmp, end=" ")
        tmp += 1
    print()