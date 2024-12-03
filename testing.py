n = [4, 6, 5, 44]

for i in range(0, len(n) - 1):
    for j in range(i -1, len(n)):
        if n[i] > n[i + 1]:
            n[i] = n[i + 1]
print(i)