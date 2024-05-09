cnt = 0
result = 0
for elem in input():
    if elem == "(":
        cnt += 1
    else:
        result += cnt

print(result)