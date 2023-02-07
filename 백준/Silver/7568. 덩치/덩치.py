N = int(input())
people = []
rank = 1
rank_ls = []
for _ in range(N):
    x, y = map(int, input().split())
    people.append((x, y))
# print(people)
for person in people:
    for j in people:
        if person[0] < j[0] and person[1] < j[1]:
            rank += 1
    rank_ls.append(rank)
    rank = 1
print(*rank_ls)