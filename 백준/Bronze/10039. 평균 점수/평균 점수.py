원섭 = int(input())
세희 = int(input())
상근 = int(input())
숭 = int(input())
강수 = int(input())
list = [원섭, 세희, 상근, 숭, 강수]

total = 0
for i in list:
    if i >= 40 :
        i = i
    else:
        i = 40
    total += i
print(int(total / len(list)))