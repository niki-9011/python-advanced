def create_playground(rows, cols):
    matrix, my_pos = [], []

    for row in range(rows):
        input_line = input().split()
        if 'B' in input_line:
            my_pos = [row, input_line.index("B")]
            input_line[my_pos[1]] = "-"
        matrix.append(input_line)

    return matrix, my_pos


def play_the_game(position, matrix):
    moves_count, touched = 0, 0
    while True:
        command = input()
        if command == "Finish":
            break

        r, c = [
            moves[command][0] + position[0],
            moves[command][1] + position[1]
        ]
        if not (0 <= r < row_size and 0 <= c < col_size):
            continue

        else:
            symbol = matrix[r][c]
            if symbol == "O":
                continue
            if symbol == 'P':
                matrix[r][c] = "-"
                touched += 1
            moves_count += 1
            position = [r, c]

        if touched == 3:
            break

    return touched, moves_count


row_size, col_size = [int(x) for x in input().split()]
moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
playground, player_pos = create_playground(row_size, col_size)
touched_quantity, moves_quantity = play_the_game(player_pos, playground)

print("Game over!")
print(f"Touched opponents: {touched_quantity} Moves made: {moves_quantity}")