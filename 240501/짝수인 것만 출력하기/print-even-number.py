n = input()
arr = list(map(int, input().split()))
arr_odd = [x for x in arr if x % 2 == 0]
print(*arr_odd)