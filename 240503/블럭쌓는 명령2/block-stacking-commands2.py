n, k = tuple(map(int, input().split()))

blocks = [0 for _ in range(n)]

for _ in range(k):
    a, b = tuple(map(int, input().split()))
    for i in range(a, b + 1):
        blocks[i] += 1        

print(max(blocks))