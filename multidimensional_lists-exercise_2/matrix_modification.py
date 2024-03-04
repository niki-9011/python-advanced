rows = int(input())

matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

while True:
    command = input().split()

    if command[0] == "END":
        break

    row, col, value = [int(x) for x in command[1:]]

    if row >= 0 and row <= rows - 1 and col >= 0 and col <= rows - 1:
        if command[0] == "Add":
            matrix[row][col] += value

        elif command[0] == "Subtract":
            matrix[row][col] -= value
    else:
        print("Invalid coordinates")

[print(*x) for x in matrix]


# rows = int(input())
#
# matrix = []
#
# for _ in range(rows):
#     matrix.append([int(x) for x in input().split()])
#
# commands = input().split()
#
# while commands[0] != "END":
#
#     command, row, col, num = (int(x) if x.isdigit() else x for x in commands)
#
#     if 0 <= int(row) <= rows - 1 and 0 <= int(col) <= rows - 1:
#         if command == "Add":
#             matrix[row][col] += num
#         elif command == "Subtract":
#             matrix[row][col] -= num
#     else:
#         print("Invalid coordinates")
#
#     commands = input().split()
#
# [print(*x) for x in matrix]