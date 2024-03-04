size = int(input())

matrix = []
bunny_row = 0
bunny_col = 0

directions = {
    "right": lambda r, c: (r, c + 1),
    "left": lambda r, c: (r, c - 1),
    "up": lambda r, c: (r - 1, c),
    "down": lambda r, c: (r + 1, c)
}

for _ in range(size):
    matrix.append(list(input().split()))

for row1 in range(size):
    for col1 in range(size):
        if matrix[row1][col1] == "B":
            bunny_row = row1
            bunny_col = col1

best_path = []
best_direct = ""
best_sum = float("-inf")

for direction in directions:
    the_sum = 0
    result = []
    row, col = directions[direction](bunny_row, bunny_col)

    while 0 <= row < size and 0 <= col < size and matrix[row][col] != "X":
        the_sum += int(matrix[row][col])
        result.append([row, col])
        row, col = directions[direction](row, col)

    if the_sum > best_sum:
        best_sum = the_sum
        best_direct = direction
        best_path = result

print(best_direct)
print(*best_path, sep="\n")
print(best_sum)

# size = int(input())
#
# matrix = [[int(x) if x.isdigit() else x for x in input().split()] for _ in range(size)]
#
# best_path = None
# bunny = []
# max_eggs = 0
# path_bunny = []
#
# positions = {"up": [-1, 0],
#              "down": [1, 0],
#              "left": [0, -1],
#              "right": [0, 1]
#              }
#
# for row in range(size):
#     for col in range(size):
#         if matrix[row][col] == "B":
#             bunny = [row, col]
#
#
# for directorate, position in positions.items():
#     row, col = [bunny[0] + position[0],
#                 bunny[1] + position[1]
#                 ]
#
#     path = []
#     egg = 0
#
#     while 0 <= row < size and 0 <= col < size:
#         if matrix[row][col] == "X":
#             break
#
#         egg += int(matrix[row][col])
#         path.append([row, col])
#
#         row += position[0]
#         col += position[1]
#
#     if egg >= max_eggs:
#         max_eggs = egg
#         best_path = directorate
#         path_bunny = path
#
# print(best_path)
# [print(x) for x in path_bunny]
# print(max_eggs)
