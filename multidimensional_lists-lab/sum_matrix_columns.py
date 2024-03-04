def get_column_sums(mm):
    columns_sums = [0] * columns_count
    for row_index in range(row_count):
        for columns_index in range(columns_count):
            columns_sums[columns_index] += mm[row_index][columns_index]

    return columns_sums


row_count, columns_count = [int(x) for x in input().split(", ")]

matrix = []

for _ in range(row_count):
    row = [int(x) for x in input().split()]
    matrix.append(row)

[print(x) for x in get_column_sums(matrix)]
