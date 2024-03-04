quantity = {"Soup": 3,
            "Pizza": 4,
            "Dessert": 2, }

products = {"Soup": [], "Pizza": [], "Dessert": []}


def shopping_cart(*args, flag=False):
    for product in args:
        if product == "Stop":
            break
        else:
            if product[0] in products and quantity[product[0]] != 0:
                if product[1] not in products[product[0]]:
                    products[product[0]] += [product[1]]
                    quantity[product[0]] -= 1
                else:
                    quantity[product[0]] -= 1

    for key, value in products.items():
        if value:
            flag = True

    if flag:
        output = ""
        for k, v in sorted(products.items(), key=lambda x: (-len(x[1]), x[0])):
            output += f'{k}:\n'

            for element in sorted(v):
                output += f' - {element}\n'

        return output

    else:
        return "No products in the cart!"


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))

# print(shopping_cart(
#     ('Pizza', 'ham'),
#     ('Dessert', 'milk'),
#     ('Pizza', 'ham'),
#     'Stop',
# ))


print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))
