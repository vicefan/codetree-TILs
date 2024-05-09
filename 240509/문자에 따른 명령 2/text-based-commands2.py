x, y = 0, 0
dxs, dys = [1, 0, -1, 0], [0, -1, 0, 1]
dirt = 3

for s in input():
    if s == "L":
        dirt = (dirt - 1) % 4
    elif s == "R":
        dirt = (dirt + 1) % 4
    else:
        x, y = x + dxs[dirt], y + dys[dirt]

print(x, y)