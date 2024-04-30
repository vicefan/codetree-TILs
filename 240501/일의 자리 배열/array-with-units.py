arr = list(map(int, input().split()))

print(*arr, end=" ")

for i in range(8):
    tmp = int(str(arr[i] + arr[i + 1])[-1])
    arr.append(tmp)
    print(tmp, end=" ")