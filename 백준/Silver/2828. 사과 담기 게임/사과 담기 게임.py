import sys

n, m = list(map(int, input().split()))
j = int(input())
apple = []
cnt = 0
for _ in range(j):
    position = int(sys.stdin.readline())
    apple.append(position)
left = 1
right = m

for i in apple:
    if i >= left and i <= right:
        continue
    elif right < i:
        cnt += i - right
        left += i - right
        right += i - right
    elif left > i:
        cnt += left - i
        right -= left - i
        left -= left - i
print(cnt)