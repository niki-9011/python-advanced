from collections import deque

textiles = deque(int(x) for x in input().split())
medicament_stack = [int(x) for x in input().split()]

collections = {30: "Patch", 40: "Bandage", 100: "MedKit"}
elements = {}

while textiles and medicament_stack:
    textile = textiles.popleft()
    medical = medicament_stack.pop()
    sum_element = textile + medical

    if sum_element in collections:
        if collections[sum_element] not in elements:
            elements[collections[sum_element]] = 1
        else:
            elements[collections[sum_element]] += 1

    elif sum_element > 100:
        resource = sum_element - 100
        el = medicament_stack.pop() + resource

        if "MedKit" not in elements:
            elements["MedKit"] = 1
        else:
            elements["MedKit"] += 1

        medicament_stack.append(el)

    else:
        medicament_stack.append(medical + 10)

if not textiles and not medicament_stack:
    print("Textiles and medicaments are both empty.")
elif not textiles:
    print("Textiles are empty.")
elif not medicament_stack:
    print("Medicaments are empty.")

for key, value in sorted(elements.items(), key=lambda x: (-x[1], x[0])):
    print(f"{key} - {value}")

if textiles:
    print(f"Textiles left: {', '.join([str(x) for x in textiles])}")
if medicament_stack:
    print(f"Medicaments left: {', '.join([str(x) for x in medicament_stack][::-1])}")
