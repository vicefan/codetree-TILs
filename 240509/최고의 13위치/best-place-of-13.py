n = int(input())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]
result = 0

for elem in arr:
    for i in range(0, n - 2):
        hap = elem[i] + elem[i + 1] + elem[i + 2]
        if hap > result:
            result = hap

print(result)