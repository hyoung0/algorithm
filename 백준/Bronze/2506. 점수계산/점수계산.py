N = int(input())
answer = map(int, input().split())

cnt = 0
list = []
for i in answer:
    if i == 1:
        list.append(i)
        len(list) * 1
        cnt += len(list)
    else:
        list = []
print(cnt)