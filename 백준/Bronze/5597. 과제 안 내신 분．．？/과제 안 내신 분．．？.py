num_list = []
for t in range(28):
    num = int(input())
    num_list.append(num)

for i in range(1, 31):
    if i not in num_list:
        print(i)