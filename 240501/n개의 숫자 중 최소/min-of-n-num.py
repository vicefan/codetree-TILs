n = int(input())
arr = list(map(int, input().split()))
print(min(arr) ,len([x for x in arr if x == min(arr)]))