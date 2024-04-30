arr_2d = [
    [x for x in input().split()]
    for _ in range(5)
]

for arr in arr_2d:
    for elem in arr:
        print(elem.upper(), end=" ")
    print()