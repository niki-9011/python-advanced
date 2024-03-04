from collections import deque

food_portions = deque(int(x) for x in input().split(", "))
staminas = deque(int(x) for x in input().split(", "))

mountains = [["Kamenitza", 70],
             ["Polezhan", 60],
             ["Banski Suhodol", 100],
             ["Kutelo", 90],
             ["Vihren", 80]
             ]

conquered_peaks = []

while food_portions and staminas and mountains:
    food = food_portions.pop()
    stamina = staminas.popleft()
    mountain = mountains.pop()

    if food + stamina >= mountain[1]:
        conquered_peaks.append(mountain[0])

    else:
        mountains.append(mountain)

if len(conquered_peaks) == 5:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")

if conquered_peaks:
    print("Conquered peaks:")
    [print(x) for x in conquered_peaks]
