num = [int(input()) for i in range(10)]

avg = sum(num) / len(num)
for i in range(len(num)):
    num[i] = (num[i], num.count(num[i]))

print(int(avg))
print(max(num, key = lambda x:x[1])[0])