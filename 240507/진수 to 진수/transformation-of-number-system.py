a, b = map(int, input().split())

arr = list(map(int, input()))

tmp = 0
cnt = 0
for elem in arr[::-1]:
     tmp += (a ** cnt) * elem
     cnt += 1

cng = []

while True:
    if tmp < b:
        cng.append(tmp)
        break
    
    cng.append(tmp % b)
    tmp = tmp // b

print(*cng[::-1], sep='')