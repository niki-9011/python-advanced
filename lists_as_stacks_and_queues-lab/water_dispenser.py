from collections import deque

watter_liters = int(input())
queue = deque()

while True:
    command = input()

    if command == "Start":
        break
    queue.append(command)

while True:
    current_command = input().split()

    if current_command[0] == "refill":
        liters = int(current_command[1])
        watter_liters += liters

    elif current_command[0] == "End":
        print(f"{watter_liters} liters left")
        break

    else:
        liters = int(current_command[0])
        person_name = queue.popleft()
        if watter_liters >= liters:
            print(f"{person_name} got water")
            watter_liters -= liters
        else:
            print(f"{person_name} must wait")
