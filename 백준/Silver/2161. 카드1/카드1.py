N = int(input())
num_list = [i for i in range(1, N + 1)]

result_list = []
while len(num_list) > 1: 
    result_list.append(num_list.pop(0))
    num_list.append(num_list.pop(0))
print(*result_list, num_list[0])