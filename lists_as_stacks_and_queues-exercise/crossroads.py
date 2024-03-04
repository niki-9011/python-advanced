from collections import deque

time_for_green = int(input())
free_window = int(input())

total_cars = 0
cars = deque()

while True:
    info = input()

    if info == "END":
        break

    elif info != "green":
        cars.append(info)

    elif info == "green":
        current_green = time_for_green

        while current_green > 0 and cars:
            car = cars.popleft()
            if len(car) > current_green + free_window:
                print(f"A crash happened!\n{car} was hit at {car[current_green + free_window]}.")
                raise SystemExit

            current_green -= len(car)
            total_cars += 1

print(f"Everyone is safe.\n{total_cars} total cars passed the crossroads."
)
