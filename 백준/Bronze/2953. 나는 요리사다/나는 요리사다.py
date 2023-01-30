matrix = [list(map(int, input().split())) for _ in range(5)]
sum_matrix = [sum(score) for score in matrix]
print(sum_matrix.index(max(sum_matrix)) + 1, max(sum_matrix))