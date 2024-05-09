x, y = 0, 0
dxs, dys = ([-1, 0, 0, 1],
            [0, -1, 1, 0])
tmp = {
    'W': 0,
    'S': 1,
    'N': 2,
    'E': 3
}

for _ in range(int(input())):
    d, n = input().split()
    n = int(n)
    x, y = x + dxs[tmp[d]] * n, y + dys[tmp[d]] * n

print(x, y)