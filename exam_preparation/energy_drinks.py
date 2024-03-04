from collections import deque

milligrams_of_caffeine = [int(x) for x in input().split(", ")]
sequence_of_energy_drinks = deque(int(z) for z in input().split(", "))

maximum_caffeine = 0

while True:
    if len(milligrams_of_caffeine) == 0 or len(sequence_of_energy_drinks) == 0:
        break
    mill_caffeine = milligrams_of_caffeine.pop()
    energy_drink = sequence_of_energy_drinks.popleft()
    caffeine = mill_caffeine * energy_drink

    if caffeine + maximum_caffeine <= 300:
        maximum_caffeine += caffeine
    else:
        if maximum_caffeine - 30 > 0:
            maximum_caffeine -= 30
        sequence_of_energy_drinks.append(energy_drink)

if sequence_of_energy_drinks:
    print(f"Drinks left: {', '.join([str(x) for x in sequence_of_energy_drinks])}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")
print(f"Stamat is going to sleep with {maximum_caffeine} mg caffeine.")
