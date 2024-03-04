from collections import deque
n = int(input())
information = deque()

fuel_stations = 0
petrol = 0
distance = 0

for info in range(n):
    information.append(input().split())

for  fuel_station in range(1, n + 1):
    petrol_station = information.popleft()

    petrol += int(petrol_station[0])
    distance += int(petrol_station[1])

    if petrol - distance >= 0:
        petrol -= distance
        distance = 0

    else:
        information.append(petrol_station)
        fuel_stations = fuel_station
        petrol = 0
        distance = 0

print(fuel_stations)
