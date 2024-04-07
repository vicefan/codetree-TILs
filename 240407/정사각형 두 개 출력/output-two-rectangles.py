n = int(input())

cnt = 0

for i in range(n * 2):
    for j in range(n):
        print("*", end='')
    print()
    cnt += 1
    if cnt == n:
        print()