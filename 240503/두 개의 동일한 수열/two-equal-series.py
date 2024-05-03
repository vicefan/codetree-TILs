N = int(input())
arr1 = sorted(set(map(int, input().split())))
arr2 = sorted(set(map(int, input().split())))

print("Yes") if arr1 == arr2 else print("No")