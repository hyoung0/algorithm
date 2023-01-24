T = int(input())
for t in range(T):
    answer = input()
    score = 0
    result = 0
    for i in answer:
        if i == "O":
            score += 1
            result += score
        else:
            score = 0
    print(result)