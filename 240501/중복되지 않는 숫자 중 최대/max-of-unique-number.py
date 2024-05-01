n = int(input())
arr = list(map(int, input().split()))

if list(set(arr)) != arr:
    arr = arr - (arr - list(set(arr)))
    print(max(arr))
else:
    print(-1)