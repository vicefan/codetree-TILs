arr = list(map(int, input().split()))

print(arr[0], arr[1], end=" ")

while True:
    if len(arr) == 10:
        break
    
    print(arr[-1] + 2 * arr[-2], end=" ")
    arr.append(arr[-1] + 2 * arr[-2])