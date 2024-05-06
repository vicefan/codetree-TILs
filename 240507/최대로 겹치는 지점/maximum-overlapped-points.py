n = int(input())
lines = [
    list(map(int, input().split()))
    for _ in range(n)
]
arr = [0 for _ in range(100)]

for elem in lines:
    for i in range(elem[0], elem[1]):
        arr[i] += 1

result = 0

print(max(arr))