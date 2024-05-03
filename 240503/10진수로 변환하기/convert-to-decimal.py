binary = list(map(int, input()))
num = 0

for i in range(len(binary)):
    num += (2 ** (len(binary) - i - 1)) * binary[i]

print(num)