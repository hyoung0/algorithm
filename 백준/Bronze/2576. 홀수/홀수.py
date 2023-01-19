odd = []
for i in range(7):
    num = int(input())
    if num % 2 == 1:
        odd.append(num)
if odd == []:
    print(-1)
else:
    print(sum(odd))
    print(min(odd))
