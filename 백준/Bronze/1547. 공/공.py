ball_list = [1, 0, 0]
M = int(input())
for _ in range(M):
    x, y = list(map(int, input().split()))
    tmp = ball_list[x-1]
    ball_list[x-1] = ball_list[y-1]
    ball_list[y-1] = tmp
print(ball_list.index(1) + 1)