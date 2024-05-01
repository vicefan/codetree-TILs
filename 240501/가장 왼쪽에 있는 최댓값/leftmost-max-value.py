n = int(input())
arr = list(map(int, input().split()))
print(arr.index(max(arr)) + 1, end=" ")

if arr.index(max(arr)) != 0:
    arr = arr[:arr.index(max(arr))]
    print(arr.index(max(arr)) + 1)