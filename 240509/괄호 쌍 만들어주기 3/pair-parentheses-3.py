arr = input()
n = len(arr)
result = 0
for i in range(n):
    for j in range(i + 1, n):
        if arr[i] + arr[j] == "()":
            result += 1

print(result)