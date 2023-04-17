def calc(n):
  zero = [1, 0, 1]
  one = [0, 1, 1]
  if len(zero) <= n:
    for i in range(len(zero), n+1):
      zero.append(zero[i-2]+zero[i-1])
      one.append(one[i-2]+one[i-1])
  return zero[n], one[n]

N = int(input())

for i in range(N):
  n = int(input())
  a, b = calc(n)
  print(a, b)