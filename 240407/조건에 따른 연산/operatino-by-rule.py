n = int(input())
cnt = 1

while True:
    if n % 2 == 0:
        n = n * 3 + 1
    else:
        n = n * 2 + 2
    
    if n >= 1000:
        break
    cnt += 1
    
print(cnt)