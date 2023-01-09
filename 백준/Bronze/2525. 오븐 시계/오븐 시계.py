a, b = map(int, input().split())
c = int(input())
h = a + ((b + c) // 60)
if h < 24:
    if (b + c) < 60:
        print(h, b + c)
    else:
        print(h, (b + c) % 60)
else:
    if (b + c) < 60:
        print(h -24, b + c)
    else:
        print(h - 24, (b + c) % 60)