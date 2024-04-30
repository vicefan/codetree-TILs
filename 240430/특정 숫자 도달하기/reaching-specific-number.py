arr = list(map(int, input().split()))
count = 0

for elem in arr:
    if elem >= 250 and count == 0:
        idx = arr.index(elem)
        print(round(sum(arr[:idx]), 1), end=" ")
        print(round(sum(arr[:idx]) / len(arr[:idx]), 1))
        count += 1

if count == 0:
    print(round(sum(arr), 1), end=" ")
    print(round(sum(arr) / len(arr), 1))