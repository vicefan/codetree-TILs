class Secret:
    def __init__(self, code, place, time):
        self.code = code
        self.place = place
        self.time = time

a, b, c = input().split()
sc = Secret(a, b, c)

print(f"""secret code : {sc.code}
meeting point : {sc.place}
time : {sc.time}""")