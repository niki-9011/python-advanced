rows, columns = [int(x) for x in input().split(", ")]

matrix = []
the_sum = 0
max_sum = 0
result = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split(", ")])

for row_index in range(rows - 1):
    for column_index in range(columns - 1):
        the_sum += matrix[row_index][column_index] + matrix[row_index + 1][column_index]\
               + matrix[row_index][column_index + 1] + matrix[row_index + 1][column_index + 1]

        if the_sum > max_sum:
            result.clear()
            max_sum = the_sum
            result = [0] * 4
            result[0] += matrix[row_index][column_index]
            result[1] += matrix[row_index + 1][column_index]
            result[2] += matrix[row_index][column_index + 1]
            result[3] += matrix[row_index + 1][column_index + 1]

        the_sum = 0

print(result[0], result[2])
print(result[1], result[3])
print(max_sum)
