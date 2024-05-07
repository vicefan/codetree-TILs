x, y = 0, 0
dx, dy = ([1, 0, -1, 0], 
          [0, -1, 0, 1])

N = int(input())
dirt = ["E", "S", "W", "N"]

arr = []
for _ in range(N):
    dir_str, dist = input().split()
    arr.append([dir_str, int(dist)])

for elem in arr:
    dir_num = dirt.index(elem[0])
    nx, ny = x + dx[dir_num] * elem[1], y + dy[dir_num] * elem[1]
    x, y = nx, ny

print(x, y)