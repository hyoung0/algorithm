N, M = map(int, input().split())
n_ls = []
m_ls = []
for _ in range(N):
    n = input()
    n_ls.append(n)
for _ in range(M):
    m = input()
    m_ls.append(m)
print(len(set(n_ls) & set(m_ls)))
for result in sorted(list(set(n_ls) & set(m_ls))):
    print(result)