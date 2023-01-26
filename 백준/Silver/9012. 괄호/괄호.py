T = int(input())
for t in range(T):
    strings = input()
    stack = []
    for string in strings:
        if string == "(":
            stack.append(string)
        else:
            if len(stack) != 0:
                stack.pop()
            else:
                print("NO")
                break
                
    else: 
        if len(stack) == 0:   
            print("YES")
        else:
            print("NO")
