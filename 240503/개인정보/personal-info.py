class People:
    def __init__(self, name, height, weight):
        self.n = name
        self.h = height
        self.w = weight

peoples = []
for _ in range(5):
    x, y, z = input().split()
    peoples.append(People(x, int(y), float(z)))

peoples.sort(key = lambda x: (x.n))

print("name")
for i in peoples:
    print(i.n, i.h, round(i.w, 1))

print()

peoples.sort(key = lambda x: (-x.h))

print("height")
for i in peoples:
    print(i.n, i.h, round(i.w, 1))