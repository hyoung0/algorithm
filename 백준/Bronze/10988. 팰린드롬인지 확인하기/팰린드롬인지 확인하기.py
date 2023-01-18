word = input()
revers_word = word[::-1]

if word[:len(word) // 2] == revers_word[:len(word) // 2]:
    print(1)
else:
    print(0)