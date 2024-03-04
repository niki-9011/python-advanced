# d yel blu e low redd

from collections import deque

words = deque(input().split())

paints = {"red", "yellow", "blue"}
other_paints = {"orange", "purple", "green"}
find_paints = []
result_paints = []
while words:
    left = words.popleft()
    right = words.pop() if words else ""

    color = left + right
    if color in paints or color in other_paints:
        find_paints.append(color)
        continue
    color = right + left
    if color in paints or color in other_paints:
        find_paints.append(color)
        continue

    left = left[:-1]
    right = right[:-1]

    if left:
        index = len(words) / 2
        words.insert(int(index), left)

    if right:
        index = len(words) / 2
        words.insert(int(index), right)

for col in find_paints:
    if col in paints:
        result_paints.append(col)
    elif col in other_paints:
        if col == "orange":
            if "red" in find_paints and "yellow" in find_paints:
                result_paints.append(col)

        elif col == "purple":
            if "red" in find_paints and "blue" in find_paints:
                result_paints.append(col)

        elif col == "green":
            if "yellow" in find_paints and "blue" in find_paints:
                result_paints.append(col)

print(result_paints)