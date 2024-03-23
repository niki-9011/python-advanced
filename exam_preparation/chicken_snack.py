from collections import deque


def eat(money, price):
    amount_money = money
    prices_foods = price

    eat_foods = 0
    pocket = 0

    input_moneys = list(map(int, amount_money.split()))
    input_foods = deque([int(x) for x in prices_foods.split()])

    while True:
        if len(input_moneys) == 0 or len(input_foods) == 0:
            break

        first_money = input_moneys.pop()
        first_price = input_foods.popleft()

        if first_money == first_price:
            eat_foods += 1

        elif first_money > first_price:
            pocket += first_money - first_price
            price_increase = input_moneys.pop() + pocket
            input_moneys.append(price_increase)
            input_foods.append(first_price)
            pocket = 0
            eat_foods += 1

        elif first_money < first_price:
            continue

    return eat_foods


def print_eat_message(eat_foods):
    if eat_foods >= 4:
        print(f"Gluttony of the day! Henry ate {eat_foods} foods.")
    elif eat_foods < 4 and eat_foods > 1:
        print(f"Henry ate: {eat_foods} foods.")
    elif eat_foods == 1:
        print(f"Henry ate: {eat_foods} food.")
    elif eat_foods == 0:
        print(f"Henry remained hungry. He will try next weekend again.")


eat_foods = eat(input(), input())
print_eat_message(eat_foods)
