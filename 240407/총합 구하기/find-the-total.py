tmp = list(map(int, input().split()))
a, b = tmp[0], tmp[1]

tot = 0
for i in range(a, b + 1):
    if i % 6 == 0 and i % 8 != 0:
        tot += i

print(tot)