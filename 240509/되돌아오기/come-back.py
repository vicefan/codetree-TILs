#            R, D, L, U
dxs, dys = ([0, 1, 0, -1], 
            [1, 0, -1, 0])

drt = {
    "N": 0,
    "E": 1,
    "S": 2,
    "W": 3
}

x, y, cnt, n = 0, 0, 1, int(input())

when = 0
while when != n:
    if x == 0 and y == 0 and cnt != 1:
        break
    d, ni = input().split()
    ni, dir_num, c = int(ni), drt[d], 0
    for _ in range(ni):
        if x == 0 and y == 0 and cnt != 1:
            continue
        else:
            x, y = x + dxs[dir_num], y + dys[dir_num]
            c += 1
    cnt += c
    when += 1

print(cnt - 1) if x == 0 and y == 0 else print(-1)