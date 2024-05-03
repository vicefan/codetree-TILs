class Product:
    def __init__(self, name="codetree", code=50):
        self.n = name
        self.c = code

ag = []
for _ in range(1):
    x, y = input().split()
    ag.append(Product(x, int(y)))

# ag.sort(key = lambda x: x.?)

print(f"""product {Product().c} is {Product().n}
product {ag[0].c} is {ag[0].n}""")