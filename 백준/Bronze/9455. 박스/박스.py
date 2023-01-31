T = int(input())
for t in range(T):
    N, M = list(map(int, input().split()))
    matrix = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for i in range(M): #열
        blank = 0
        for j in range(N-1,-1,-1): #행
            if blank < 1 and matrix[j][i] == 1:
                pass
            elif matrix[j][i] == 0:
                blank += 1
            elif matrix[j][i] == 1:
                matrix[j+blank][i] = 1
                matrix[j][i] = 0
                result += blank
    print(result)