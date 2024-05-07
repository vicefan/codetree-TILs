n = int(input())
arr = [list(map(int, input().split()))
for _ in range(n)]

dxs, dys = ([1, 0, -1, 0], 
          [0, -1, 0, 1])

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

result = 0

for i in range(n):
    for j in range(n):
        cnt = 0
        for dx, dy in zip(dxs, dys):
            x, y = i + dx, j + dy
            if in_range(x, y) and arr[x][y] == 1:
                cnt += 1
        if cnt >= 3:
            result += 1

print(result)