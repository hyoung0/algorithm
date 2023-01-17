x_list = []
y_list = []
for i in range(3):
    x, y = list(map(int, input().split()))
    x_list.append(x)
    y_list.append(y)

for i in range(3):
    if x_list.count(x_list[i]) == 1:
        X = x_list[i]
    if y_list.count(y_list[i]) == 1:
        Y = y_list[i]
print(X, Y)
   