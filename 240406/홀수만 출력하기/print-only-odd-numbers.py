n = int(input())

for i in range(n):
    tmp = int(input())
    if tmp % 2 == 1 and tmp % 3 == 0:
        print(tmp)