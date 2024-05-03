n = int(input())

arr = [100 for _ in range(200)]

for _ in range(n):
    a, b = tuple(map(int, input().split()))
    for i in range(a + 1, b):
        arr[i] += 1

print(max(arr) - 100)