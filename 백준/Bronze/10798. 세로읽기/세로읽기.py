matrix = []
for i in range(5):
    string = list(input())
    if len(string) != 15:
        string += [""] * (15 - len(string))
    matrix.append(string)
        
new = [[""] * 5 for _ in range(15)]

for i in range(15):
    for j in range(5):
        new[i][j] = matrix[j][i]

for i in new:
    print(''.join(i), end='')