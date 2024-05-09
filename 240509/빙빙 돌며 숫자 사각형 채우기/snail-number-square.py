#            R, D, L, U
dxs, dys = ([0, 1, 0, -1], 
            [1, 0, -1, 0])

n, m = map(int, input().split())
arr = [
    [0 for _ in range(n)]
    for _ in range(m)
    ]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

x, y, dir_num, cnt = 0, 0, 0, 2
arr[x][y] = 1

for _ in range(n * m - 1):
    nx, ny = x + dxs[dir_num], y + dys[dir_num]
    if not in_range(nx, ny) or arr[nx][ny] != 0:
        dir_num = (dir_num + 1) % 4
        nx, ny = x + dxs[dir_num], y + dys[dir_num]

    arr[nx][ny] = cnt
    x, y = nx, ny
    cnt += 1

for elem in arr:
    print(*elem)