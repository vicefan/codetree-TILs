arr_2d = [
    [arr for arr in list(map(int, input().split()))]
    for _ in range(4)
]

sum_val = 0

for a in range(4):
    for b in range(a + 1):
        sum_val += arr_2d[a][b]

print(sum_val)