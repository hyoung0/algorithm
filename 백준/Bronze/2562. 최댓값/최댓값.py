numbers = []
for i in range(9):
    num = int(input())
    numbers.append(num)
n_max = max(numbers)
print(n_max, numbers.index(n_max) + 1, sep="\n")