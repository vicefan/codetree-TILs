n = int(input())
arr = []
field =[0 for _ in range(300)]
start = 150

for _ in range(n):
    x, d = input().split()
    arr.append([int(x), d])

for elem in arr:
    if elem[1] == "R":
        m = elem[0] + start
        for i in range(start, m + 1):
            field[i] += 1
            start = m
    else:
        m = start - elem[0]
        for i in range(m, start - 1, -1):
            field[i] += 1
            start = m

total = 0

for elem in field:
    if elem >= 2:
        total += elem

print(total)