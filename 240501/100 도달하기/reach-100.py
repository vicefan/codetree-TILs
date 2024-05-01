n = int(input())
arr = [1, n]

print(arr[0], n, end=" ")

while True:
    if arr[-1] > 100:
        break
    
    print(arr[-1] + arr[-2], end=" ")
    arr.append(arr[-1] + arr[-2])