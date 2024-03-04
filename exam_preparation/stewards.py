from collections import deque

seats = input().split(", ")
first_deque = deque(map(int, input().split(", ")))
second_deque = deque(map(int, input().split(", ")))

seat_matches = []
rotations_count = 0

for x in range(1, 10 + 1):
    if len(seat_matches) == 3:
        break

    rotations_count = x
    first_num = first_deque.popleft()
    second_num = second_deque.pop()
    character = first_num + second_num

    if str(first_num) + chr(character) in seats and str(first_num) + chr(character) not in seat_matches:
        seat_matches.append(str(first_num) + chr(character))

    elif str(second_num) + chr(character) in seats and str(second_num) + chr(character) not in seat_matches:
        seat_matches.append(str(second_num) + chr(character))

    else:
        first_deque.append(first_num)
        second_deque.appendleft(second_num)

print(f"Seat matches: {', '.join(seat_matches)}")
print(f"Rotations count: {rotations_count}")
