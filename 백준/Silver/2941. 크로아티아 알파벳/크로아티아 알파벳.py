string = input()
change = change = ["c=", "c-","dz=","d-","lj", 'nj', 's=','z=']
for i in change:
    string = string.replace(i, "*")
print(len(string))