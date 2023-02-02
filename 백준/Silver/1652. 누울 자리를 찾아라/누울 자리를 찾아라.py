N = int(input())
matrix = [list(input()) for _ in range(N)]

cnt = 0
for i in range(N):
    length = 0
    for j in range(N):
        if matrix[i][j] == ".":
            length += 1
        if matrix[i][j] == "X" or j == N-1:
            if length >= 2:
                cnt += 1
            length = 0

cnt2 = 0
for i in range(N):
    length = 0
    for j in range(N):
        if matrix[j][i] == ".":
            length += 1
        if matrix[j][i] == "X" or j == N-1:
            if length >= 2:
                cnt2 += 1
            length = 0
print(cnt, cnt2)