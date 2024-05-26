def feed_snake(row, col):
    global food, snake_pos
    snake_pos = [row, col]
    food += 1


def snake_burrow(row, col):
    global snake_pos, territory, burrows_pos
    territory[row][col] = '.'
    if burrows_pos[0] == [row, col]:
        snake_pos = burrows_pos[1]
    else:
        snake_pos = burrows_pos[0]


def move_snake(row, col):
    global snake_pos
    snake_pos = [row, col]


size = int(input())

actions = {'*': feed_snake,
           'B': snake_burrow,
           '-': move_snake}

territory = []
snake_pos = []
burrows_pos = []
moves = {"up": (-1, 0), "down": (1, 0),
         "left": (0, -1), "right": (0, 1)}

for row in range(size):
    line = list(input())
    if 'S' in line:
        snake_pos = [row, line.index('S')]
    for col in range(size):
        symbol = line[col]
        if symbol == 'B':
            burrows_pos.append([row, col])
    territory.append(line)

food = 0
while True:
    way = input()
    territory[snake_pos[0]][snake_pos[1]] = '.'
    snake_row = snake_pos[0] + moves[way][0]
    snake_col = snake_pos[1] + moves[way][1]

    if 0 <= snake_row < size and 0 <= snake_col < size:
        symbol = territory[snake_row][snake_col]
        actions[symbol](snake_row, snake_col)

    else:
        break
    territory[snake_pos[0]][snake_pos[1]] = 'S'
    if food == 10:
        break
print("Game over!" if food < 10 else "You won! You fed the snake.")
print(f'Food eaten: {food}')
print('\n'.join(''.join(row) for row in territory))

