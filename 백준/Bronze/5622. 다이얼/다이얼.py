cnt = 0
string = input()
alpha_list = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
for i in string:
    for j in range(len(alpha_list)):
        if i in alpha_list[j]:
            num = j + 2
            cnt += num
print(cnt + len(string))