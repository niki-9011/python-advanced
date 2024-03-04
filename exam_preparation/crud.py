row, col = 6, 6

matrix = [[x for x in input().split()] for _ in range(row)]

coordinate = input()

position = [coordinate[1], coordinate[4]]
position = list(map(int, position))

directions = {"up": lambda x, y: (x - 1, y),
              "down": lambda x, y: (x + 1, y),
              "right": lambda x, y: (x, y + 1),
              "left": lambda x, y: (x, y - 1)
              }

while True:
    command = input().split(", ")

    if command[0] == "Stop":
        break

    elif command[0] == "Create":
        row, col = directions[command[1]]((position[0]), position[1])
        if matrix[row][col] == ".":
            matrix[row][col] = command[2]

        position = [row, col]

    elif command[0] == "Update":
        row, col = directions[command[1]]((position[0]), position[1])
        if matrix[row][col] != ".":
            matrix[row][col] = command[2]

        position = [row, col]
    elif command[0] == "Delete":
        row, col = directions[command[1]]((position[0]), position[1])
        if matrix[row][col] != ".":
            matrix[row][col] = "."

        position = [row, col]
    elif command[0] == "Read":
        row, col = directions[command[1]]((position[0]), position[1])
        if matrix[row][col] != ".":
            print(matrix[row][col])
        position = [row, col]

[print(*x) for x in matrix]
