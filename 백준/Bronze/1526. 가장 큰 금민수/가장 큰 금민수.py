N = list(range(4, int(input()) + 1))

num = []
for n in N:
    cnt = 0
    for i in str(n):
        if i == '4' or i == '7':
            cnt += 1
    if cnt == len(str(n)):
        num.append(n)
print(max(num))