n = int(input())
arr = list(map(int, input().split()))

cnt = 0
for elem in arr:
    if arr.count(elem) > 1:
        arr.remove(elem)
        cnt += 1

if cnt == 0:
    print(-1)
else:
    print(max(arr))