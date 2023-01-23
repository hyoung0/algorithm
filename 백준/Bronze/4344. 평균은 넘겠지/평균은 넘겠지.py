C = int(input())
for c in range(C):
    score = list(map(int, input().split()))
    score.pop(0)
    avg = sum(score) / len(score)
    cnt = 0
    for i in score:
        if i > avg:
            cnt += 1
    print(f'{cnt / len(score) * 100:.3f}%')