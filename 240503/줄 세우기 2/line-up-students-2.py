class People:
    def __init__(self, height, weight, number):
        self.h = height
        self.w = weight
        self.n = number

peoples = []
for _ in range(int(input())):
    x, y = map(int, input().split())
    peoples.append(People(x, y, _ + 1))

peoples.sort(key = lambda x: (x.h, -x.w))

for i in peoples:
    print(i.h, i.w, i.n)