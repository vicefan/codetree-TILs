class Who:
    def __init__(self, name, address, area):
        self.n = name
        self.a = address
        self.r = area

ag = []
for _ in range(int(input())):
    x, y, z = input().split()
    ag.append(Who(x, y, z))

ag.sort(key = lambda x: x.n, reverse=True)

print(f"""name {ag[0].n}
addr {ag[0].a}
city {ag[0].r}""")