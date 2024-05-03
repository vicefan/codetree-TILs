n = int(input())
arr = list(map(int, input().split()))
count = 1
for elem in arr:
    if count % 2 == 1:
        idx = arr.index(elem)
        tmp = sorted(arr[:idx+1])
        print(tmp[int((len(tmp)-1)/2)], end = " ")
    count += 1