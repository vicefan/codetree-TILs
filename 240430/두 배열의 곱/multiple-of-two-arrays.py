arr_1 = [
    [x for x in list(map(int, input().split()))]
    for _ in range(3)
]

blank = input()

arr_2 = [
    [x for x in list(map(int, input().split()))]
    for _ in range(3)
]


for x in range(3):
    for y in range(3):
        print(arr_1[x][y] * arr_2[x][y], end=" ")
    print()