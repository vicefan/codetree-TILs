m1, d1, m2, d2 = map(int, input().split())

num_of_days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

yo = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

what_yo = yo.index(input()) + 1

yoyo, tmp = 0, 1

while True:
    if m1 == m2 and d1 == d2:
        break
    
    if d1 == num_of_days[m1] + 1:
        d1 = 1
        m1 += 1

    if tmp == what_yo:
        yoyo += 1
    
    if tmp == 7:
        tmp = 1

    d1 += 1
    tmp += 1
    
print(yoyo)