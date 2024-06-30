size = 6
moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
deposits = {'M': 'Metal', 'W': 'Water', 'C': 'Concrete'}

mars = []
rover_location = []
founded_deposits = set()
for row in range(size):
    line = input().split()
    if 'E' in line:
        rover_location = [row, line.index('E')]
        line[rover_location[1]] = '-'
    mars.append(line)

command_line = input().split(', ')

for direction in command_line:
    rover_row = rover_location[0] + moves[direction][0]
    rover_col = rover_location[1] + moves[direction][1]

    if rover_row < 0:
        rover_row = size - 1
    elif rover_row == size:
        rover_row = 0
    elif rover_col < 0:
        rover_col = size - 1
    elif rover_col == size:
        rover_col = 0

    symbol = mars[rover_row][rover_col]
    if symbol in deposits:
        material = deposits[symbol]
        founded_deposits.add(material)
        print(f"{material} deposit found at ({rover_row}, {rover_col})")
    elif symbol == 'R':
        print(f"Rover got broken at ({rover_row}, {rover_col})")
        break
    rover_location = [rover_row, rover_col]

if len(founded_deposits) < 3:
    print("Area not suitable to start the colony.")
else:
    print("Area suitable to start the colony.")


# Input
# - R - - - -
# - - - - - R
# - E - R - -
# - W - - - -
# - - - C - -
# M - - - - -
# down, right, down, right, down, left, left, left
