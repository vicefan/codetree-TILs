class S:
    def __init__(self, name, a, b, c):
        self.name = name
        self.a = a
        self.b = b
        self.c = c

ss = []

for _ in range(int(input())):
    i = input().split()
    n, x, y, z = i
    ss.append(S(n, int(x), int(y), int(z)))

ss.sort(key=lambda s:s.a + s.b + s.c)

for s in ss:
    print(s.name, s.a, s.b, s.c)