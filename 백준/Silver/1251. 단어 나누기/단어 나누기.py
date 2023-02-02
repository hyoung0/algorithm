string = input()
re_ls = []
for i in range(1, len(string) - 1):
    for j in range(i + 1, len(string)):
        re = string[:i][::-1] + string[i:j][::-1] + string[j:][::-1]
        re_ls.append(re)
print(sorted(re_ls)[0])
