size = int(input())
number_car = input()

car_position = [0, 0]
distance = 0
flag = False
matrix = [[x for x in input().split()] for z in range(size)]

directions = {"up": lambda r, c: (r - 1, c),
              "down": lambda r, c: (r + 1, c),
              "left": lambda r, c: (r, c - 1),
              "right": lambda r, c: (r, c + 1)
              }

command = input()

while command != "End" and command:
    if command in directions:
        row, col = directions[command](car_position[0], car_position[1])
        car_position = [row, col]

        if matrix[row][col] == "T":
            matrix[row][col] = "."
            distance += 30

            for r in range(size):
                for c in range(size):
                    if matrix[r][c] == "T":
                        car_position = [r, c]
                        matrix[r][c] = "."

        elif matrix[row][col] == "F":
            matrix[row][col] = "C"
            distance += 10
            print(f"Racing car {number_car} finished the stage!")
            flag = True
            break

        else:
            if matrix[row][col] == ".":
                car_position = [row, col]
                distance += 10

    command = input()

matrix[car_position[0]][car_position[1]] = "C"

if not flag:
    print(f"Racing car {number_car} DNF.")

print(f"Distance covered {distance} km.")

[print("".join(x)) for x in matrix]
