x, y = 0, 0
dx, dy = ([1, -1, 0, 0], 
          [0, 0, -1, 1])

N = int(input())
dirt = ["E", "W", "S", "N"]

for _ in range(N):
    dir_str, dist = input().split()
    dist = int(dist)
    dir_num = dirt.index(dir_str)
    nx, ny = x + dx[dir_num] * dist, y + dy[dir_num] * dist
    x, y = nx, ny

print(x, y)