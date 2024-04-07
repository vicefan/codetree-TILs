arr = list(map(int, input().split()))
a, b = tuple(arr)

count = 0

for i in range(a, b + 1):
    if 1920 % i == 0 and 2880 % i == 0:
        print(1)
        count += 1
        break

if count == 0:
    print(0)