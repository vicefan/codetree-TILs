r, c = map(int, input().split())
arr = [
    input().split()
    for _ in range(c)
]
route = []

x, y, color = 0, 0, arr[0][0]

for _ in range(2):
    color = arr[0][0]
    for i in range(1, r):
        for j in range(1, c):
            color_diff = arr[i][j]
            if color == color_diff:
                pass
            else:
                route.append((i, j,))
                x, y = i, j
                color = color_diff
    

print(route.count((4, 4)))