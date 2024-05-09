import sys

n = int(input())
arr = list(map(int, input().split()))
result = sys.maxsize

for i in range(n):
    tmp = 0
    for j in range(n):
        tmp += abs(i - j) * arr[j]
    if tmp <= result:
        result = tmp

print(result)