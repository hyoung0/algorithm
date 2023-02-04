from collections import Counter

word = input().upper()
cnt = Counter(word)
cnt_value = []

for key in cnt:
    cnt_value.append(cnt[key])
max_cnt = max(cnt_value)
if cnt_value.count(max_cnt) > 1:
    print("?")
else:
    for key, value in cnt.items():
        if value == max_cnt:
            print(key)