arr = list(map(int, input().split()))

if 999 in arr:
    arr = arr[:arr.index(999)]
elif -999 in arr:
    arr = arr[:arr.index(-999)]

print(max(arr), min(arr))