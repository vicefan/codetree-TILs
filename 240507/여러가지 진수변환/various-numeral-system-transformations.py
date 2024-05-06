n, b = map(int, input().split())
tmp = []

while True:
    if n < b:
        tmp.append(n)
        break
    
    tmp.append(n % b)
    n = n // b

print(*tmp[::-1], sep='')