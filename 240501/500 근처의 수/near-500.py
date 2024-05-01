arr = list(map(int, input().split()))

arr1 = [x for x in arr if x < 500]
arr2 = [x for x in arr if x >= 500]

print(max(arr1), min(arr2))