import sys

N = int(sys.stdin.readline())
books = []
book_cnt = []
for _ in range(N):
    book = input()
    books.append(book)
for i in set(books):
    book_cnt.append((i, books.count(i)))

book_cnt = sorted(book_cnt, key = lambda x : x[0])
print(max(book_cnt, key = lambda x : x[1])[0])