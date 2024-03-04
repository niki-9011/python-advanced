stack_of_clothes = input().split()
capacity = int(input())

rack = 1
value = 0

while True:
    if len(stack_of_clothes) == 0:
        break

    clothes = int(stack_of_clothes.pop())

    if value + clothes <= capacity:
        value += clothes
    else:
        value = 0
        rack += 1
        value += clothes

print(rack)
