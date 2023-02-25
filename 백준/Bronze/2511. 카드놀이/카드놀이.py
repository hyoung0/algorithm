a = list(map(int, input().split()))
b = list(map(int, input().split()))
a_result = 0
b_result = 0
ls = []

for i in range(10):
    if a[i] > b[i]:
        a_result += 3
        ls.append('A')
    elif a[i] == b[i]:
        a_result += 1
        b_result += 1
        ls.append('D')
    else:
        b_result += 3
        ls.append('B')
print(a_result, b_result)

if a_result > b_result:
    print('A')
elif a_result < b_result:
    print('B')
else:
    if 'A' in ls or 'B' in ls:
        for j in range(9,0,-1):
            if ls[j] == 'B':
                print('B')
                break
            elif ls[j] == 'A':
                print('A')
                break
    else:
        print('D')