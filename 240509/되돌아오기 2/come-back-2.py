#            R, D, L, U
dxs, dys = ([0, 1, 0, -1], 
            [1, 0, -1, 0])

x, y, cnt, dir_num = 0, 0, 0, 0

for elem in input():
    if x == 0 and y == 0 and cnt != 0:
        continue
    else:
        if elem == "R":
            dir_num = (dir_num + 1) % 4
        elif elem == "L":
            dir_num = (dir_num - 1) % 4
        else:
            x, y = x + dxs[dir_num], y + dys[dir_num]
        cnt += 1

print(cnt) if x == 0 and y == 0 else print(-1)