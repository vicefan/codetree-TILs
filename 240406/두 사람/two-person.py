info1 = input().split()
info2 = input().split()

if (int(info1[0]) >= 19 and info1[1] == "M") or (int(info2[0]) >= 19 and info2[1] == "M"):
    print(1)
else:
    print(0)