#            R, D, L, U
dxs, dys = ([0, 1, 0, -1], 
            [1, 0, -1, 0])

n, m = map(int, input().split())

arr = [
    [0 for x in range(n)]
    for x in range(n)
]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

for _ in range(m):
    x, y = map(int, input().split())
    x, y = x - 1, y - 1
    arr[x][y] = 1
    cnt = 0
    for dx, dy in zip(dxs, dys):
        if in_range(x + dx, y + dy) and arr[x + dx][y + dy] == 1:
            cnt +=1
    print(1) if cnt == 3 else print(0)