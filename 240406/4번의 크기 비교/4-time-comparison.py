a = int(input())
tmp = list(map(int, input().split()))

for i in tmp:
    if a > i:
        print(1)
    else:
        print(0)