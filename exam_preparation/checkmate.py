size = 8
directions = {
    'u': (-1, 0), 'ul': (-1, -1), 'ur': (-1, 1),
    'd': (1, 0), 'dl': (1, -1), 'dr': (1, 1),
    'l': (0, -1), 'r': (0, 1)}

board = []
queens_positions = []
king = []

for row in range(size):
    line = input().split()
    board.append(line)

    if 'K' in line:
        king = [row, line.index('K')]

for way in directions.values():
    king_row, king_col = king
    while True:
        row = king_row + way[0]
        col = king_col + way[1]

        if 0 <= row < size and 0 <= col < size:
            symbol = board[row][col]
            if symbol == 'Q':
                queens_positions.append([row, col])
                break
        else:
            break
        king_row, king_col = row, col
if queens_positions:
    print(*queens_positions, sep='\n')
else:
    print('The king is safe!')


# Input
# . . . . . . . .
# . . . Q . . . .
# . . . . . . . .
# . . . . . . . .
# Q . . . Q . . .
# . . K . . . . .
# . . . . . . Q .
# . . . Q . . . .