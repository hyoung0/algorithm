A, B = input().split()
answer_A = A[::-1]
answer_B = B[::-1]
if int(answer_A) > int(answer_B):
    print(answer_A)
else:
    print(answer_B)