n = int(input())
di = 1
count = 0
while n > 1:
    count += 1
    n = n / di
    di += 1
print(count)