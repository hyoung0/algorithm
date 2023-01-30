matrix = [list(i) for i in list(input().split())] 
num1 = sum(list(map(int, matrix[0])))
num2 = sum(list(map(int, matrix[1])))
print(num1 * num2)