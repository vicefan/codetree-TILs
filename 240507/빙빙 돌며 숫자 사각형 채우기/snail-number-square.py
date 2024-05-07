dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

n, m = map(int, input().split())
arr = [
    [0 for _ in range(m)]
    for _ in range(n)
]

dir_num = 0

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

r, c = 0, 0
arr[r][c] = 1

for i in range(2, n * m + 1):
    nr, nc = r + dxs[dir_num], c + dys[dir_num]
    if (not in_range(nr, nc)) or arr[nr][nc] != 0:
        dir_num = (dir_num + 1) % 4
        nr, nc = r + dxs[dir_num], c + dys[dir_num]
    
    r, c = nr, nc
    arr[r][c] = i


for elem in arr:
    print(*elem)