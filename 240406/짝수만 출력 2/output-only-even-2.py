tmp = list(map(int, input().split()))

b, a = tuple(tmp)

goal = a
num = b

while num != goal:
    print(num, end=' ')
    num -= 2

print(goal)