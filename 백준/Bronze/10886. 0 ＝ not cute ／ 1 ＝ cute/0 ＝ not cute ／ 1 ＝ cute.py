N = int(input())
cnt_cute = 0
cnt_no = 0

for n in range(N):
    op = int(input())
    if op == 1:
        cnt_cute += 1
    else:
        cnt_no += 1
if cnt_cute > cnt_no:
    print("Junhee is cute!")
else:
    print( "Junhee is not cute!")