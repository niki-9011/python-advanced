rows, columns = [int(x) for x in input().split()]

matrix = []
squares = 0

for _ in range(rows):
    matrix.append([str(x) for x in input().split()])

for row_index in range(rows - 1):
    for column_index in range(columns - 1):
        if matrix[row_index][column_index] == matrix[row_index + 1][column_index] ==\
                matrix[row_index][column_index + 1] == matrix[row_index + 1][column_index + 1]:
            squares += 1

print(squares)
