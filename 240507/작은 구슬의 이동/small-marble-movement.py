n, t = map(int, input().split())
dxs, dys = ([0, 1, -1, 0], 
            [1, 0, 0, -1])

dr = {
    'R': 0,
    'U': 1,
    'D': 2,
    'L': 3
}

def in_range(x, y):
    return 1 <= x < n and 1 <= y < n

r, c, d = input().split()
r, c = int(r), int(c)
d_num = dr[d]

for _ in range(t):
    if in_range(r + dxs[d_num], c + dys[d_num]):
        r, c = r + dxs[d_num], c + dys[d_num]
    else:
        d_num = 3 - d_num

print(r, c)