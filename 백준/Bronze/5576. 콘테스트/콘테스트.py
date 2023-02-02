W = []
K = []
for _ in range(10):
    w = int(input())
    W.append(w)
for _ in range(10):
    k = int(input())
    K.append(k)
w_sorted = sorted(W)[-3:]
k_sorted = sorted(K)[-3:]
print(sum(w_sorted), sum(k_sorted))
