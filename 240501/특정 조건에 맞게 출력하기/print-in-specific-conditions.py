arr = list(map(int, input().split()))

if 0 in arr:
    arr = arr[:arr.index(0)]

for elem in arr:
    print(elem + 3, end=" ") if elem % 2 == 1 else print(elem // 2, end=" ")