n = int(input())

arr = [0 for _ in range(201)]

for _ in range(n):
    a, b = tuple(map(int, input().split()))
    a, b = a + 100, b + 100
    for i in range(a + 1, b + 1):
        arr[i] += 1

print(max(arr))