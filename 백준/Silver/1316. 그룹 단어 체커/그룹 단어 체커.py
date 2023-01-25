N = int(input())
for n in range(N):
    word = input()
    string_list = []
    
    for string in word:
        if string not in string_list:
            string_list.append(string)
        else:
            if string == string_list[-1]:
                string_list.append(string)
            else:
                N -= 1
                break
print(N)