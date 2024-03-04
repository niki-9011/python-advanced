rows, columns = [int(x) for x in input().split()]

mm = []
position = []

moves = 0
players = 0

directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

for row in range(rows):
    mm.append(input().split())

    if 'B' in mm[row]:
        position = [row, mm[row].index('B')]

while players < 3:
    command = input()

    if command == 'Finish':
        break

    r, c = position[0] + directions[command][0], position[1] + directions[command][1]

    if not (0 <= r < rows and 0 <= c < columns):
        continue

    elem = mm[r][c]

    if elem == 'O':
        continue

    elif elem == 'P':
        mm[r][c] = '-'
        players += 1

    moves += 1
    position = [r, c]

print("Game over!")
print(f"Touched opponents: {players} Moves made: {moves}")
