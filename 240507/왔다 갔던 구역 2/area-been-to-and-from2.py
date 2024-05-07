n = int(input())
arr = [0 for _ in range(300)]
dm = []

for _ in range(n):
    a, b = input().split()
    dm.append([int(a), b])

current = 150
dest = 0

for d in dm:
    if d[1] == "R":
        dest = current + d[0]
        for i in range(current, dest):
            arr[i] += 1
            current = dest
    else:
        dest = current - d[0]
        for i in range(current, dest, -1):
            arr[i] += 1
            current = dest

cnt = 0
for elem in arr:
    if elem >= 2:
        cnt += 1

print(cnt)