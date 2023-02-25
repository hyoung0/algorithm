import sys
N, M = list(map(int, sys.stdin.readline().split()))
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
k = int(sys.stdin.readline())
for _ in range(k):
    i, j, x, y = list(map(int, sys.stdin.readline().split()))
    result = 0
    for row in range(i-1, x):
        for col in range(j-1,y):
            result += matrix[row][col]
    print(result)
