class Weather:
    def __init__(self, date, yo, wea):
        self.d = date
        self.y = yo
        self.w = wea

ag = []
for _ in range(int(input())):
    x, y, z = input().split()
    if z == "Rain":
        ag.append(Weather(x, y, z))

ag.sort(key = lambda x: tuple(map(int, x.d.split("-"))))

print(ag[0].d, ag[0].y, ag[0].w)