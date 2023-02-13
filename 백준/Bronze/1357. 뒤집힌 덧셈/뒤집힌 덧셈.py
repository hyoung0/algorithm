x, y = input().split()
def rev(x):
    return int(x[::-1])
a = rev(x) + rev(y)
print(rev(str(a)))