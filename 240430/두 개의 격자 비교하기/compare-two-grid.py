n, m = tuple(map(int, input().split()))

arr_1 = [
    [x for x in list(map(int, input().split()))]
    for _ in range(n)
]

arr_2 = [
    [x for x in list(map(int, input().split()))]
    for _ in range(n)
]

for i in range(n):
    for j in range(m):
        print(0, end=" ") if arr_1[i][j] == arr_2[i][j] else print(1, end=" ")
    print()