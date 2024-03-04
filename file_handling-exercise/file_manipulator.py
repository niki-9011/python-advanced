import os

while True:
    command = input().split("-")

    if command[0] == "End":
        break

    elif command[0] == "Create":
        file = open(command[1], "w")
        file.close()

    elif command[0] == "Add":
        file = open(f"{command[1]}", "a")
        file.write(f"{command[2]}\n")
        file.close()

    elif command[0] == "Replace":
        try:
            with open(f"{command[1]}", "r") as file:
                file_text = file.read()

            file_text = file_text.replace(command[2], command[3])

            with open(f"{command[1]}", "w") as file:
                text = file.write("".join(file_text))

        except FileNotFoundError:
            print("An error occurred")

    elif command[0] == "Delete":
        try:
            os.remove(f"{command[1]}")

        except FileNotFoundError:
            print("An error occurred")

