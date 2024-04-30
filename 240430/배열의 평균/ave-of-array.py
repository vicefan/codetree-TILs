arr_2d = [
    [x for x in list(map(int, input().split()))]
    for _ in range(2)
]

for arr in arr_2d:
    print(f"{sum(arr) / len(arr):.1f}", end=" ")

print()

for x in range(4):
    print(f"{(arr_2d[0][x] + arr_2d[1][x]) / 2:.1f}", end=" ")

print()

sum_v = 0
len_arr = 0
for x in range(2):
    sum_v += sum(arr_2d[x])
    len_arr += len(arr_2d[x])

print(f"{sum_v / len_arr:.1f}")