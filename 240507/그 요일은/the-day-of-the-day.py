m1, d1, m2, d2 = map(int, input().split())

num_of_days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

yo = ["", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

days, cnt, idx = 1, 0, yo.index(input())

while True:
    if m1 == m2 and d1 == d2 + 1:
        break
    
    if d1 > num_of_days[m1]:
        d1 = 1
        m1 += 1

    if days % 7 == idx or (days % 7 == 0 and idx == 7):
        cnt += 1
    
    d1 += 1
    days += 1

print(cnt)