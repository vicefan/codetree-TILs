arr_2d = [
    [0 for _ in range(2001)]
    for _ in range(2001)
]

cnt = 0
for _ in range(3):
    x1, y1, x2, y2 = tuple(map(lambda x :int(x)+1000, input().split()))

    if cnt == 2:
        for x in range(x1, x2):
            for y in range(y1, y2):
                arr_2d[x][y] = 0
    else:
        for x in range(x1, x2):
            for y in range(y1, y2):
                arr_2d[x][y] = 1
    cnt += 1

all = 0

for arr in arr_2d:
    all += sum(arr)

print(all)