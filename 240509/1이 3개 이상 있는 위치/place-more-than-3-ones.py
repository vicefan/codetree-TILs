dxs = [0, 1,  0, -1]
dys = [1, 0, -1,  0]
n = int(input())

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

result = 0

for j in range(n):
    for i in range(n):
        cnt = 0
        for x in range(4):
            nx, ny = i + dxs[x], j + dys[x]
            if in_range(nx, ny) and arr[nx][ny] == 1:
                cnt += 1
        if cnt >= 3:
            result += 1

print(result)