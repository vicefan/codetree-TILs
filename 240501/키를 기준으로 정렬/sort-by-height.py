class Size:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

n = int(input())

sizes = []

for _ in range(n):
    x = input().split()
    n, h, w = x
    sizes.append(Size(n, int(h), int(w)))

sizes.sort(key=lambda x: x.height)

for s in sizes:
    print(s.name, s.height, s.weight)