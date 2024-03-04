size = int(input())

matrix = []
primary = []
secondary = []

for _ in range(size):
    matrix.append([int(x) for x in input().split()])

for index in range(size):
    primary.append(matrix[index][index])
    secondary.append(matrix[index][size - 1 - index])

print(abs(sum(primary) - sum(secondary)))


# n = int(input())
#
# matrix = [[int(x) for x in input().split()] for _ in range(n)]
# primary_diagonal = [matrix[r][r] for r in range(n)]
# secondary_diagonal = [matrix[(n - 1) - r][r] for r in range(n - 1, - 1, -1)]
#
# print(abs(sum(primary_diagonal)- sum(secondary_diagonal)))
