n = int(input())
arr = list(map(int, input().split()))
arr_tmp = []
cnt = 0
for elem in arr:
    if arr.count(elem) > 1:
        cnt += 1
    else:
        arr_tmp.append(elem)

if cnt == 0 or len(arr_tmp) == 0:
    print(-1)
else:
    print(max(arr_tmp))