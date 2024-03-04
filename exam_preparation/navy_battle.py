size = int(input())

matrix = [[x for x in input()] for z in range(size)]

submarine = []
cruisers = 0
mines = 0

directions = {"up": lambda r, c: (r - 1, c),
               "down": lambda r, c: (r + 1, c),
               "left": lambda r, c: (r, c - 1),
               "right": lambda r, c: (r, c + 1)
               }

for row in range(size):
    for col in range(size):
        if matrix[row][col] == "S":
            submarine.append(row)
            submarine.append(col)

        elif matrix[row][col] == "C":
            cruisers += 1

command = input()

while cruisers > 0 and command and mines < 3:
    matrix[submarine[0]][submarine[1]] = "-"

    if command in directions:
        row, col = directions[command](submarine[0], submarine[1])
        submarine = [row, col]

        if matrix[submarine[0]][submarine[1]] == "*":
            mines += 1

        elif matrix[submarine[0]][submarine[1]] == "C":
            cruisers -= 1

        matrix[row][col] = "S"

    command = input()

if cruisers == 0:
    print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")

if mines == 3:
    print(f"Mission failed, U-9 disappeared! Last known coordinates [{submarine[0]}, {submarine[1]}]!")

[print("".join(x)) for x in matrix]
