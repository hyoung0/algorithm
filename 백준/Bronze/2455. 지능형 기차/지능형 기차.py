cnt = 0
ls = []

for _ in range(4):
    a, b = list(map(int, input().split()))
    cnt = cnt - a + b
    ls.append(cnt)
print(max(ls))