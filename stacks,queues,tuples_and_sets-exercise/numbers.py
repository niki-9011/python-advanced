first_numbers = set(int(x) for x in input().split())
second_number = set(int(z) for z in input().split())

n = int(input())

commands = {
    "Add First": lambda x: [first_numbers.add(el) for el in x],
    "Add Second": lambda x: [second_number.add(el) for el in x],
    "Remove First": lambda x: [first_numbers.discard(el) for el in x],
    "Remove Second": lambda x: [second_number.discard(el) for el in x],
    "Check Subset": lambda: print(True) if first_numbers.issubset(second_number)
    or second_number.issubset(first_numbers) else print(False)
}

for _ in range(n):
    command, *data = input().split()
    current_command = command + " " + data.pop(0)


    if data:
        commands[current_command]([int(x) for x in data])
    else:
        commands[current_command]()

print(*sorted(first_numbers), sep=", ")
print(*sorted(second_number), sep=", ")
