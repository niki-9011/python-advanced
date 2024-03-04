from collections import deque

heroes = deque(input().split(", "))

size = 6

matrix = [[x for x in input().split()] for z in range(size)]

current_coordinate = input()

hero_dict = {"Tom": 0, "Jerry": 0}

while current_coordinate:

    coordinates = current_coordinate.strip("()")
    row, col = coordinates.split(", ")
    row = int(row)
    col = int(col)

    hero = heroes.popleft()

    if hero_dict[hero] != 0:
        hero_dict[hero] -= 1
        heroes.append(hero)

        current_coordinate = input()
        continue

    else:
        if matrix[row][col] == "E":
            print(f"{hero} found the Exit and wins the game!")
            break

        elif matrix[row][col] == "T":
            print(f"{hero} is out of the game! The winner is {''.join(heroes)}.")
            break

        elif matrix[row][col] == "W":
            hero_dict[hero] += 1
            print(f"{hero} hits a wall and needs to rest.")

        heroes.append(hero)

    current_coordinate = input()
