arr = list(map(int, input().split()))

if 0 in arr:
    arr = arr[:arr.index(0)]
    arr = arr[::-1]
    print(*arr)
else:
    print(*arr)