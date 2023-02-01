T = int(input())
for t in range(T):
    scores = list(map(int, input().split()))
    scores = sorted(scores)
    scores.pop(0)
    scores.pop(3)
    if scores[2] - scores[0] >= 4:
        print("KIN")
    else:
        print(sum(scores))