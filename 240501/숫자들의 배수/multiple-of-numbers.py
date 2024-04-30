n = int(input())

cnt = 0
i = 1
while True:
    if cnt == 2:
        break
    if n * i % 5 == 0:
        cnt += 1
    
    print(n * i, end=" ")
    i += 1