n = int(input())

arr = [x for x in list(map(int, input().split())) if x % 2 == 0]

print(*arr)