N = int(input())
load = list(map(int, input().split()))
tmp = [] 
uphill = []  

for i in load:
    if tmp == []:
        tmp.append(i)
    elif i > tmp[-1]:
        tmp.append(i)
    else:
        if len(tmp) > 1:
            uphill.append(tmp[-1] - tmp[0])
        tmp = []
        tmp.append(i)
if len(tmp) > 1:
    uphill.append(tmp[-1] - tmp[0])

if uphill == []:
    print(0)
else:
    print(max(uphill))