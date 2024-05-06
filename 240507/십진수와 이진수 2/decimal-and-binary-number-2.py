arr = list(map(int, input()))

tmp = 0
cnt = 0
for elem in arr[::-1]:
     tmp += (2 ** cnt) * elem
     cnt += 1
    
tmp = tmp * 17

cng = []

while True:
    if tmp < 2:
        cng.append(tmp)
        break
    
    cng.append(tmp % 2)
    tmp = tmp // 2

print(*cng[::-1], sep='')