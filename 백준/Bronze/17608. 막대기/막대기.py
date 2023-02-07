import sys

n = int(sys.stdin.readline())
h_ls = []
for _ in range(n):
    h = int(sys.stdin.readline())
    h_ls.append(h)

standard = h_ls[-1]
cnt = 0
for elem in h_ls[::-1]:
    if elem > standard:
        cnt += 1
        standard = elem

print(cnt + 1)