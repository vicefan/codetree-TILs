n = int(input())
arr = list(map(int, input().split()))
print(arr.index(max(arr)) + 1, end=" ")
arr = arr[:arr.index(max(arr))]

while True:
    if len(arr) <= 1:
        break
    print(arr.index(max(arr)) + 1, end=" ")
    arr = arr[:arr.index(max(arr))]