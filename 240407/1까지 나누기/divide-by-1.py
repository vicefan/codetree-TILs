n = int(input())
di = 1
count = 0
while True:
    if n <= 1:
        break
    count += 1
    n = n // di
    di += 1
print(count)