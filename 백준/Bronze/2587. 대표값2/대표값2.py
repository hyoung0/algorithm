num_list = []
for t in range(5):
    num = int(input())
    num_list.append(num)
print(int(sum(num_list) / len(num_list)))
print(sorted(num_list)[2])