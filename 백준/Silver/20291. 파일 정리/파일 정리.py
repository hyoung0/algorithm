from collections import Counter

N = int(input())
files = []
result = []
for i in range(N):
    name, file = input().split('.')
    files.append(file)
cnt = Counter(files)
for key, values in cnt.items():
    result.append((key, values))
result = sorted(result, key=lambda x : x[0]) 

for file_, cnt in result:
     print(file_, cnt)