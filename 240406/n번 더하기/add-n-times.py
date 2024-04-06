tmp = list(map(int, input().split()))

a, n = tuple(tmp)

for i in range(n):
    a += n
    print(a)