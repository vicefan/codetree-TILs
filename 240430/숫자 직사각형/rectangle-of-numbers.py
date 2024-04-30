n, m = tuple(map(int, input().split()))

arr_2d = [
    [0 for _ in range(m)] 
    for _ in range(n)
]

cnt = 1

for i in range(n):
    for j in range(m):
        arr_2d[i][j] = cnt
        cnt += 1

for arr in arr_2d:
    print(*arr)