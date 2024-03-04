def shop_from_grocery_list(budget, grocery_list, *products):
    remaining_budget = budget
    purchased_items = set()
    missing_items = set(grocery_list)

    for product, price in products:
        if product in missing_items and remaining_budget >= price:
            remaining_budget -= price
            purchased_items.add(product)
            missing_items.remove(product)
        elif remaining_budget < price:
            break

    if not missing_items:
        return f"Shopping is successful. Remaining budget: {remaining_budget:.2f}."
    else:
        return f"You did not buy all the products. Missing products: {', '.join(missing_items)}."


print(shop_from_grocery_list(
    100,
    ["tomato", "cola"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("tomato", 20.45),
))

print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("meat", 22),
))

print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat", "chocolate"],
    ("cola", 15.8),
    ("chocolate", 30),
    ("tomato", 15.85),
    ("chips", 50),
    ("meat", 22.99),
))
