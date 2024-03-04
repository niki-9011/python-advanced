def command_is_valid(row, col, rows, coulumns):
    return row < 0 or col < 0 or row >= rows or col >= coulumns


rows, columns = [int(x) for x in input().split()]
matrix = []

for _ in range(rows):
    matrix.append([x for x in input().split()])

while True:
    command = input()
    if command == "END":
        break

    current_command = command.split()

    if len(current_command) != 5 or current_command[0] != "swap":
        print("Invalid input!")
        continue

    row1, col1, row2, col2 = [int(x) for x in current_command[1:]]

    if command_is_valid(row1, col1, rows, columns) or command_is_valid(row2, col2, rows, columns):
        print("Invalid input!")
        continue

    matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]

    for z in matrix:
        print(*z, sep=" ")

# row, col = [int(x) for x in input().split()]
# matrix = []
#
# for _ in range(row):
#     matrix.append([x for x in input().split()])
#
# while True:
#     command = input().split()
#     if command[0] == "END":
#         break
#
#     if command[0] == "swap" and len(command) == 5 and 0 <= int(command[1]) <= row and 0 <= int(command[2]) <= col and 0 <= int(command[3])<= row and 0 <= int(command[4]) <= col:
#
#         matrix[int(command[1])][int(command[2])], matrix[int(command[3])][int(command[4])] = matrix[int(command[3])][int(command[4])], matrix[int(command[1])][int(command[2])]
#
#         [print(*x) for x in matrix]
#
#     else:
#         print("Invalid input!")
#         continue
