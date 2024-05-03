class Agent:
    def __init__(self, name, score):
        self.name = name
        self.score = score

ag = []
for _ in range(5):
    x, y = input().split()
    ag.append(Agent(x, int(y)))

ag.sort(key = lambda x: x.score)

print(ag[0].name, ag[0].score)