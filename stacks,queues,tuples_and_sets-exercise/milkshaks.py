from collections import deque


def print_func(chocolates, cups_of_milk, milkshakes):
    if milkshakes == 5:
        print("Great! You made all the chocolate milkshakes needed!")
    else:
        print("Not enough milkshakes.")

    if chocolates:
        print(f"Chocolate: {', '.join(str(x) for x in chocolates)}")
    else:
        print(f"Chocolate: empty")

    if cups_of_milk:
        print(f"Milk: {', '.join(str(x) for x in cups_of_milk)}")
    else:
        print(f"Milk: empty")


def milkshake(chocolates, cups_of_milk):
    milkshakes = 0
    while True:
        if not chocolates or not cups_of_milk or milkshakes == 5:
            break

        choco = chocolates.pop()
        milk = cups_of_milk.popleft()

        if choco == milk:
            milkshakes += 1

        else:
            if choco <= 0:
                cups_of_milk.appendleft(milk)
                continue
            elif milk <= 0:
                chocolates.append(choco)
                continue
            else:
                cups_of_milk.append(milk)
                chocolates.append(choco - 5)

    print_func(chocolates, cups_of_milk, milkshakes)


chocolate_stack = [int(x) for x in input().split(", ")]
cups_of_milks = deque(int(x) for x in input().split(", "))

milkshake(chocolate_stack, cups_of_milks)


# from collections import deque
#
# chocolates_stack = [int(x) for x in input().split(", ")]
# cups_of_milk = deque([int(n) for n in input().split(", ")])
#
# milkshake = 0
#
# while chocolates_stack and cups_of_milk and milkshake < 5:
#
#     chocolate = chocolates_stack.pop()
#     milk = cups_of_milk.popleft()
#
#     if milk <= 0 and chocolate <= 0:
#         continue
#
#     if chocolate <= 0:
#         cups_of_milk.appendleft(milk)
#         continue
#
#     if milk <= 0:
#         chocolates_stack.append(chocolate)
#         continue
#
#     if chocolate == milk:
#         milkshake += 1
#     else:
#         cups_of_milk.append(milk)
#         chocolates_stack.append(chocolate - 5)
#
# if milkshake == 5:
#     print("Great! You made all the chocolate milkshakes needed!")
# else:
#     print("Not enough milkshakes.")
#
# if chocolates_stack:
#     print(f"Chocolate: {', '.join(str(i) for i in chocolates_stack)}")
# else:
#     print("Chocolate: empty")
#
# if cups_of_milk:
#     print(f"Milk: {', '.join(str(i) for i in cups_of_milk)}")
# else:
#     print("Milk: empty")
