N = int(input())
tmp = N
cnt = 0
while True:
    N_1 = N // 10 + N % 10
    N_2 = (N % 10) * 10  + N_1 % 10
    cnt += 1

    N = N_2
    if N == tmp:
        break
print(cnt)