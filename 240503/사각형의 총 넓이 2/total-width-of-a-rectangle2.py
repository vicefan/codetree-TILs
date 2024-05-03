arr_2d = [
    [0 for _ in range(201)]
    for _ in range(201)
]

for _ in range(int(input())):
    x1, y1, x2, y2 = tuple(map(int, input().split()))
    x1, y1, x2, y2 = x1 + 100, y1 + 100, x2 + 100, y2 + 100
    for i in range(y1, y2):
        for j in range(x1, x2):
            arr_2d[i][j] = 1

all = 0

for arr in arr_2d:
    all += sum(arr)

print(all)