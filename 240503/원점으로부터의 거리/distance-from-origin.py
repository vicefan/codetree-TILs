class Distance:
    def __init__(self, x, y, number):
        self.x = x
        self.y = y
        self.n = number

distances = []

for i in range(int(input())):
    a, b = tuple(map(int, input().split()))
    distances.append(Distance(a, b, i + 1))

distances.sort(key = lambda a: a.x + a.y)

for i in distances:
    print(i.n)