def cookbook(*args):

    cuisine_recipes = {}

    for recipe in args:
        name, cuisine, ingredients = recipe
        if cuisine not in cuisine_recipes:
            cuisine_recipes[cuisine] = []
        cuisine_recipes[cuisine].append((name, ingredients))

    sorted_cuisines = sorted(cuisine_recipes.items(), key=lambda x: (-len(x[1]), x[0]))

    for cuisine, recipes in sorted_cuisines:
        print(f"{cuisine} cuisine contains {len(recipes)} recipes:")
        # Sort recipes within each cuisine alphabetically
        sorted_recipes = sorted(recipes, key=lambda x: x[0])
        for recipe in sorted_recipes:
            recipe_name, ingredients = recipe
            print(f"  * {recipe_name} -> Ingredients: {', '.join(ingredients)}")


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
