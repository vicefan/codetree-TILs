test = False

for i in range(5):
    a = int(input())
    if a % 3 != 0:
        test = True

if test == False:
    print(1)
else:
    print(0)