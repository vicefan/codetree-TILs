n = int(input())
arr = list(map(int, input().split()))
arr_tmp = []
cnt = 0
for elem in arr:
    if arr.count(elem) > 1:
        cnt += 1
    else:
        arr_tmp.append(elem)

if cnt == 0:
    print(max(arr_tmp))
else:
    print(-1)