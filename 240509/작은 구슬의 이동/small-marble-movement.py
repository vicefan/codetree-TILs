dxs = [0, 1,  0, -1]
dys = [-1, 0, 1,  0]

n, t = map(int, input().split())
r, c, d = tuple(input().split())
r, c = int(r), int(c)

dr = {
    "D": 0,
    "R": 1,
    "L": 2,
    "U": 3
}

arr = [
    [0 for _ in range(n)]
    for _ in range(n)
    ]

def in_range(x, y):
    return 1 <= x < n and 1 <= y < n

for _ in range(t):
    dir_str = dr[d]
    nr, nc = r + dxs[dir_str], c + dys[dir_str]
    if not in_range(nr, nc):
        dir_str = 3 - dir_str
    else:
        r, c = nr, nc

print(r, c)