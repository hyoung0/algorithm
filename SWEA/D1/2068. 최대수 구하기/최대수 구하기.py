T = int(input())

for t in range(1, T + 1):
    num = list(map(int, input().split()))
    max = num[0]
    for i in num:
        if max < i:
            max = i
    print(f"#{t} {max}")