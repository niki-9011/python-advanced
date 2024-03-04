number_car = int(input())

cars = set()

for num in range(number_car):
    direction, car_number = input().split(", ")
    if direction == "IN":
        cars.add(car_number)

    elif direction == "OUT":
        cars.remove(car_number)

if cars:
    for car in cars:
        print(car)
else:
    print("Parking Lot is Empty")
