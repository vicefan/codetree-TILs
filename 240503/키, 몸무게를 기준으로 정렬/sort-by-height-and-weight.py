class People:
    def __init__(self, name, height, weight):
        self.n = name
        self.h = height
        self.w = weight

peoples = []
for _ in range(int(input())):
    x, y, z = input().split()
    peoples.append(People(x, int(y), int(z)))

peoples.sort(key = lambda x: (x.h, -x.w))

for i in peoples:
    print(i.n, i.h, i.w)