n = int(input())
arr = [0 for _ in range(200000)]
dm = []

for _ in range(n):
    a, b = input().split()
    dm.append([int(a), b])

start = 100000
dest = 0

for d in dm:
    if d[1] == "R":
        dest = start + d[0] - 1
        for i in range(start, dest + 1):
            arr[i] = 1
            start = dest
    else:
        dest = start - d[0] + 1
        for i in range(start, dest - 1, -1):
            arr[i] = -1
            start = dest

print(arr.count(-1), arr.count(1))