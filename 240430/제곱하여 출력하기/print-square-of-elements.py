n = int(input())
arr = [x ** 2 for x in list(map(int, input().split()))]
print(*arr)