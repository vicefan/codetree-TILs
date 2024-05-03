N = int(input())
arr = sorted(list(map(int, input().split())))

while True:
    if len(arr) == 2:
        print(sum(arr))
        break
    arr.pop(arr.index(max(arr)))
    arr.pop(arr.index(min(arr)))