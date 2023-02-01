N = int(input())
string = '666'
cnt = 0
n = 666

while True:
    if string in str(n):
        cnt += 1
    if cnt == N:
        print(n)
        break    
    n += 1