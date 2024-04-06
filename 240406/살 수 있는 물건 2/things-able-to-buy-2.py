money = int(input())
book, mask, pen = 3000, 1000, 500

if money >= book:
    print("book")
elif money >= mask:
    print("mask")
elif money >= pen:
    print("pen")
else:
    print("no")