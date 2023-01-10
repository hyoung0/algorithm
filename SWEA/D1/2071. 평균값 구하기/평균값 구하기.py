T = int(input())

for t in range(1,T + 1):
    num = list(map(int, input().split()))
    total = 0
    for i in num:
        total += i
    print(f"#{t} {round(total / len(num))}")