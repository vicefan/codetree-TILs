money = int(input())

book, mask = 3000, 1000

if money >= book:
    print("book")
elif money >= mask:
    print("mask")
else:
    print("no")