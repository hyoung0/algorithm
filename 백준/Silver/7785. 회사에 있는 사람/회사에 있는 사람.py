N = int(input())
record_dict = {}
for n in range(N):
    name, record = input().split()
    if record == "enter":
        record_dict[name] = record
    else:
        record_dict.pop(name)

record_dict = sorted(record_dict.keys(), reverse = True)

for i in record_dict:
    print(i)