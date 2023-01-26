N = int(input())
number_list = []
numbers = list(map(int, input().split()))
cnt = 0
for number in numbers:
    if number not in number_list:
        number_list.append(number)
    else:
        cnt += 1
print(cnt)