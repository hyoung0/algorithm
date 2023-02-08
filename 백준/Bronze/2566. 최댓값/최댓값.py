matrix = [list(map(int, input().split())) for _ in range(9)]
max_num = 0
for row in matrix:
    if max(row) > max_num:
        max_num = max(row)
print(max_num)

for i in range(9):
    for j in range(9):
        if matrix[i][j] == max_num:
            print(i+1, j+1)
            break