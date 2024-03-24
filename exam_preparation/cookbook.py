def cookbook(*args):
    cuisine_recipes = {}

    for recipe in args:
        name, cuisine, ingredients = recipe
        if cuisine not in cuisine_recipes:
            cuisine_recipes[cuisine] = []
        cuisine_recipes[cuisine].append((name, ingredients))

    sorted_cuisines = sorted(cuisine_recipes.items(), key=lambda x: (-len(x[1]), x[0]))

    output = ""
    for cuisine, recipes in sorted_cuisines:
        output += f"{cuisine} cuisine contains {len(recipes)} recipes:\n"
        recipes.sort(key=lambda x: x[0])  # Sorting recipes by name
        for recipe in recipes:
            ingredients_str = ", ".join(recipe[1])
            output += f"  * {recipe[0]} -> Ingredients: {ingredients_str}\n"

    return output.strip()


# Test cases
print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"])
))

print(cookbook(
    ("Pad Thai", "Thai", ["rice noodles", "shrimp", "peanuts", "bean sprouts", "tamarind sauce"])
))

print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"]),
    ("Sushi Rolls", "Japanese", ["rice", "nori", "fish", "vegetables"]),
    ("Miso Soup", "Japanese", ["tofu", "seaweed", "green onions"]),
    ("Guacamole", "Mexican", ["avocado", "tomato", "onion", "lime"])
))
