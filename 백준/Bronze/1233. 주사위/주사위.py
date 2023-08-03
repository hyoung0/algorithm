import sys
s1,s2,s3=map(int,sys.stdin.readline().split())
tmp=[0]*81
for i in range(1,s1+1):
    for j in range(1, s2 + 1):
        for k in range(1, s3 + 1):
            tmp[i+j+k]+=1
for i in range(1,81):
    if tmp[i]==max(tmp):
        print(i); break