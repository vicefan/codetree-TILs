#            R, D, L, U
dxs, dys = ([0, 1, 0, -1], 
            [1, 0, -1, 0])

n = int(input())

arr = [
    list(input())
    for x in range(n)
]

k = int(input())
k_ = k % n
if 1 <= k <= n:
    dir_num = 1
    x, y = 0, k_ - 1
elif n + 1 <= k <= 2*n:
    dir_num = 2
    x, y = k_ - 1, n - 1
elif 2*n + 1 <= k <= 3*n:
    dir_num = 3
    x, y = n - 1, n - k_
else:
    dir_num = 0
    x, y = 0, n - k_

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

# R, D, L, U
cnt = 0
while in_range(x, y):
    if arr[x][y] == "/":
        if dir_num == 1 or dir_num == 3:
            dir_num = (dir_num + 1) % 4
        else:
            dir_num = (dir_num - 1) % 4
    else:
        if dir_num == 1 or dir_num == 3:
            dir_num = (dir_num - 1) % 4
        else:
            dir_num = (dir_num + 1) % 4
    x, y = x + dxs[dir_num], y + dys[dir_num]
    cnt += 1

print(cnt)