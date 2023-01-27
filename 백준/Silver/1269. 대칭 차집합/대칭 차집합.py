a, b = list(map(int, input().split()))
a_ = set(list(map(int, input().split())))
b_ = set(list(map(int, input().split())))
print(len(a_ ^ b_))