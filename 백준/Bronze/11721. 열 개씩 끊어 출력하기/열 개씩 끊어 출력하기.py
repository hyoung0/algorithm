n = input()
n = list(n)

for i in range(len(n)):
    if (i + 1) % 10 == 0:
        print(n[i])
    else:
        print(n[i], end="")