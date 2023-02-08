N, M = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(N)]
b = [list(map(int, input().split())) for _ in range(N)]
matrix = [[0] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        matrix[i][j] = a[i][j] + b[i][j]
for row in matrix:
    print(*row)