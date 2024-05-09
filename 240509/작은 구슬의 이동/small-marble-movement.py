dxs, dys = ([1, 0, 0, -1], 
            [0, 1, -1, 0])
dr = {
    "D": 0,
    "R": 1,
    "L": 2,
    "U": 3
}

n, t = map(int, input().split())
r, c, d = tuple(input().split())
r, c, dir_str = int(r), int(c), dr[d]

def in_range(x, y):
    return 1 <= x < n and 1 <= y < n

for _ in range(t):
    nr, nc = r + dxs[dir_str], c + dys[dir_str]
    if in_range(nr, nc):
        r, c = nr, nc
    else:
        dir_str = 3 - dir_str

print(r, c)