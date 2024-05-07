x, y = 0, 0
dir_num = 3
dx, dy = ([1, -1, 0, 0], 
          [0, 0, -1, 1])

for d in input():
    if d == "L":
        dir_num = (dir_num - 1) % 4
    elif d == "R":
        dir_num = (dir_num + 1) % 4
    else:
        x, y = x + dx[dir_num], y + dy[dir_num]

print(x, y)