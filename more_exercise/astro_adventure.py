def solve(teams):
    astronauts_count = int(teams.pop(0))
    astronauts = {}

    for _ in range(astronauts_count):
        name, oxygen, energy = teams.pop(0).split()
        astronauts[name] = [int(oxygen), int(energy)]

    while teams:
        command, astronaut_name, astronaut_energy = teams.pop(0).split(' - ')

        if command == "End":
            break

        if command == "Explore":
            if int(astronaut_energy) <= astronauts[astronaut_name][1]:
                energy_left_explore = astronauts[astronaut_name][1] - int(astronaut_energy)
                print(f"{astronaut_name} has successfully explored a new area and now has {energy_left_explore} energy!")
                astronauts[astronaut_name][1] = energy_left_explore
            else:
                print(f"{astronaut_name} does not have enough energy to explore!")

        elif command == "Refuel":
            if astronauts[astronaut_name][1] <= 200:
                energy_left_refuel = astronauts[astronaut_name][1] + int(astronaut_energy)
                if energy_left_refuel >= 200:
                    print(f"{astronaut_name} refueled their energy by {200 - astronauts[astronaut_name][1]}!")
                    astronauts[astronaut_name][1] = 200
                elif energy_left_refuel < 200:
                    print(f"{astronaut_name} refueled their energy by {energy_left_refuel}!")
                    astronauts[astronaut_name][1] = energy_left_refuel

        elif command == "Breathe":
            if int(astronauts[astronaut_name][0]) <= 100:
                oxygen_left = astronauts[astronaut_name][0] + int(astronaut_energy)
                if oxygen_left >= 100:
                    print(f"{astronaut_name} took a breath and recovered 100 oxygen!")
                    astronauts[astronaut_name][0] = 100
                elif oxygen_left < 100:
                    print(f"{astronaut_name} took a breath and recovered {oxygen_left} oxygen!")
                    astronauts[astronaut_name][0] = oxygen_left

    for name, stats in astronauts.items():
        oxygen, energy = stats
        print(f"Astronaut: {name}, Oxygen: {oxygen}, Energy: {energy}")

solve(['3',
    'John 50 120',
    'Kate 80 180',
    'Rob 70 150',
    'Explore - John - 50',
    'Refuel - Kate - 30',
    'Breathe - Rob - 20',
    'End'])

solve(['4',
    'Alice 60 100',
    'Bob 40 80',
    'Charlie 70 150',
    'Dave 80 180',
    'Explore - Bob - 60',
    'Refuel - Alice - 30',
    'Breathe - Charlie - 50',
    'Refuel - Dave - 40',
    'Explore - Bob - 40',
    'Breathe - Charlie - 30',
    'Explore - Alice - 40',
    'End'])
