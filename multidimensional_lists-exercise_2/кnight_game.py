def find_count(boards, rows, cols):
    moves = [
        [row - 2, col - 1],
        [row - 1, col - 2],
        [row - 1, col + 2],
        [row - 2, col + 1],
        [row + 1, col - 2],
        [row + 2, col - 1],
        [row + 1, col + 2],
        [row + 2, col + 1]
    ]

    result = 0

    for r, c in moves:
        if 0 <= r < len(boards) and 0 <= c < len(boards) and board[r][c] == "K":
            result += 1

    return result


size = int(input())

board = []

for _ in range(size):
    board.append(list(input()))

remove_knight_counter = 0

while True:
    best_count = 0
    knight_row = 0
    knight_col = 0

    for row in range(size):
        for col in range(size):
            if board[row][col] == "0":
                continue

            count = find_count(board, row, col)
            if count > best_count:
                best_count = count
                knight_row = row
                knight_col = col

    if best_count == 0:
        break

    board[knight_row][knight_col] = "0"
    remove_knight_counter += 1

print(remove_knight_counter)


# size = int(input())
# matrix = [list(input()) for _ in range(size)]

# positions = ((-2, -1),
#              (-2, 1),
#              (2, -1),
#              (2, 1),
#              (-1, 2),
#              (-1, -2),
#              (1, 2),
#              (1, -2)
#              )
#
# knight_removed = 0
#
# while True:
#     max_attacks = 0
#     knight_position = []
#
#     for row in range(size):
#         for col in range(size):
#             if 0 <= row < size and 0 <= col < size:
#                 if matrix[row][col] == "K":
#                     attack = 0
#                 else:
#                     continue
#
#                 for position in positions:
#                     pos_row = row + position[0]
#                     pos_col = col + position[1]
#
#                     if 0 <= pos_row < size and 0 <= pos_col < size:
#                         if matrix[pos_row][pos_col] == "K":
#                             attack += 1
#
#                     if attack > max_attacks:
#                         knight_position = [row, col]
#                         max_attacks = attack
#
#     if knight_position:
#         matrix[knight_position[0]][knight_position[1]] = "0"
#         knight_removed += 1
#     else:
#         break
#
# print(knight_removed)
