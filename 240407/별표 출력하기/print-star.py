n = int(input())
cnt = 1

while True:
    print("* " * cnt)
    if cnt == n:
        break
    else:
        cnt += 1

for i in range(n - 1):
    cnt -= 1
    print("* " * cnt)