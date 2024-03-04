size = int(input())

matrix = []
primary = []
secondary = []

for _ in range(size):
    matrix.append([int(x) for x in input().split(", ")])

for index in range(size):
    primary.append(matrix[index][index])
    secondary.append(matrix[index][size - 1 - index])

result_primary = ", ".join([str(x) for x in primary])
result_secondary = ", ".join([str(x) for x in secondary])

print(f"Primary diagonal: {result_primary}. Sum: {sum(primary)}")
print(f"Secondary diagonal: {result_secondary}. Sum: {sum(secondary)}")
