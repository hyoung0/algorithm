x = int(input())

total = 0
n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    total += a * b

if total == x:
    print("Yes")
else:
    print("No")
    