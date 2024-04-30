arr = list(map(int, input().split()))

if 0 in arr:
    arr = arr[:arr.index(0)]

arr_sum = [x for x in arr if x % 2 == 0]

print(f"{len(arr_sum)} {sum(arr_sum)}")