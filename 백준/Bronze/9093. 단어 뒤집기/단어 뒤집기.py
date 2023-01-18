T = int(input()) 

for t in range(T):
    sentence = input().split()
    result_list = []
    for word in sentence:
        new_word = word[::-1]
        result_list.append(new_word)
    print(' '.join(result_list))