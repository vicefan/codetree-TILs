tmp = []
while True:
    a = int(input())
    if 20 <= a <= 29:
        tmp.append(a)
    else:
        break

print(f"{sum(tmp) / len(tmp):.2f}")