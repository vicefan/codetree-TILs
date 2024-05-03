binary = list(map(int, input()))
num = 0

for x in range(len(binary)):
   num = num * 2 + binary[x]

print(num)