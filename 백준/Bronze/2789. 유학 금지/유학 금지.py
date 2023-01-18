strings = input()
new_list = []
for string in strings:
    if string not in 'CAMBRIDGE':
        new_list.append(string)
result = ''.join(new_list)
print(result)