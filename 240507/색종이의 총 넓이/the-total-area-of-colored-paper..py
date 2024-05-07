n = int(input())

arr_2d = [
    [0 for _ in range(201)]
    for _ in range(201)
]

arr = [
    list(map(lambda x:int(x) + 100, input().split()))
    for _ in range(n)
]

for elem in arr:
    for i in range(elem[0], elem[0] + 8):
        for j in range(elem[1], elem[1] + 8):
            arr_2d[i][j] = 1

result = 0

for elem in arr_2d:
    result += sum(elem)

print(result)