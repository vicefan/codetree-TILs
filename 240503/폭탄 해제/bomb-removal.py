class Bomb:
    def __init__(self, code, color, second):
        self.c = code
        self.o = color
        self.s = second

ag = []
for _ in range(1):
    x, y, z = input().split()
    ag.append(Bomb(x, y, int(z)))

# ag.sort(key = lambda x: x.?)

print(f"""code : {ag[0].c}
color : {ag[0].o}
second : {ag[0].s}""")