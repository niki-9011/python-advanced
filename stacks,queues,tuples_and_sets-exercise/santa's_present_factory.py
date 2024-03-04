import sys
from io import StringIO
from collections import deque

# input1 = '''10 -5 20 15 -30 10
# 40 60 10 4 10 0
# '''
# input2 = '''30 5 15 60 0 30
# -15 10 5 -15 25
# '''
# input3 = '''30 10
# 15 10 5 0 10
# '''
toys = {150: "Doll",
        250: "Wooden train",
        300: "Teddy bear",
        400: "Bicycle"
        }

made_toys = {}

# sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)
# sys.stdin = StringIO(input3)

materials_stack = [int(x) for x in input().split()]
magic_level = deque([int(n) for n in input().split()])

while materials_stack and magic_level:
    product = 0
    material = materials_stack.pop()
    magic_number = magic_level.popleft()

    if material == 0 and magic_number == 0:
        continue

    if material == 0:
        magic_level.appendleft(magic_number)
        continue

    if magic_number == 0:
        materials_stack.append(material)
        continue

    if material * magic_number < 0:
        materials_stack.append(material + magic_number)

    elif material * magic_number > 0:
        product = material * magic_number

        if product not in toys:

            if product > 0:
                materials_stack.append(material + 15)
                product = 0
        else:
            if toys[product] not in made_toys:
                made_toys[toys[product]] = 1
            else:
                made_toys[toys[product]] += 1
                product = 0

if "Doll" in made_toys and "Wooden train" in made_toys:
    print("The presents are crafted! Merry Christmas!")

elif "Teddy bear" in made_toys and "Bicycle" in made_toys:
    print("The presents are crafted! Merry Christmas!")

else:
    print("No presents this Christmas!")

if materials_stack:
    print(f"Materials left: {', '.join(map(str, materials_stack[::-1]))}")

if magic_level:
    print(f"Magic left: {', '.join(map(str, magic_level))}")

for key, value in sorted(made_toys.items()):
    print(f"{key}: {value}")
