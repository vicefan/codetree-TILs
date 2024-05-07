mapper = {
    'R': 0,
    'D': 1,
    'U': 2,
    'L': 3
}

dxs, dys = ([0, 1, -1, 0], 
            [1, 0, 0, -1])

n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r), int(c)
dir_num = mapper[d]


def in_range(x, y):
    return 1 <= x <= n and 1 <= y <= n


for _ in range(t):
    nr, nc = r + dxs[dir_num], c + dys[dir_num]
    if in_range(nr, nc):
        r, c = nr, nc
    else:
        dir_num = 3 - dir_num

print(r, c)