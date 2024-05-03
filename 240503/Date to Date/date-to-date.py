a, b, c, d = tuple(map(int, input().split()))

num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

elapsed_days = 0

while True:
    if a == c and b == d + 1:
        break

    elapsed_days += 1
    b += 1

    if b > num_of_days[a]:
        a += 1
        b = 1

print(elapsed_days)