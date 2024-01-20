def cook_recipe(recipe_name, pantry):
    if recipe_name not in recipes:
        print("Recipe not found.")
        return

    recipe_ingredients = recipes[recipe_name]
    for ingredient in recipe_ingredients:
        if ingredient not in pantry or pantry[ingredient] <= 0:
            print(f"Insufficient quantity of {ingredient} in the pantry.")
            return

    print(f"Cooking {recipe_name}...")
    for ingredient in recipe_ingredients:
        pantry[ingredient] -= 1

    print(f"{recipe_name} is ready!")

def display_menu():
    print("Available Recipes:")
    for recipe_name in recipes.keys():
        print(f"- {recipe_name}")
    print("Enter 'exit' to quit.")

def display_pantry(pantry):
    print("\nPantry Inventory:")
    for item, quantity in pantry.items():
        print(f"{item}: {quantity}")

if __name__ == "__main__":
    pantry = {
        "chicken": 500,
        "lemon": 2,
        "cumin": 24,
        "paprika": 18,
        "chilli powder": 7,
        "yogurt": 300,
        "oil": 450,
        "onion": 5,
        "garlic": 9,
        "ginger": 2,
        "tomato puree": 125,
        "almonds": 75,
        "rice": 500,
        "coriander": 20,
        "lime": 3,
        "pepper": 8,
        "egg": 6,
        "pizza": 2,
        "spam": 1,
    }

    recipes = {
        "Butter chicken": [
            "chicken",
            "lemon",
            "cumin",
            "paprika",
            "chilli powder",
            "yogurt",
            "oil",
            "onion",
            "garlic",
            "ginger",
            "tomato puree",
            "almonds",
            "rice",
            "coriander",
            "lime",
        ],
        "Chicken and chips": [
            "chicken",
            "potatoes",
            "salt",
            "malt vinegar",
        ],
        "Pizza": [
            "pizza",
        ],
        "Egg sandwich": [
            "egg",
            "bread",
            "butter",
        ],
        "Beans on toast": [
            "beans",
            "bread",
        ],
        "Spam a la tin": [
            "spam",
            "tin opener",
            "spoon",
        ],
    }

    while True:
        display_menu()
        choice = input("Enter the name of the recipe you want to cook: ")

        if choice.lower() == "exit":
            break

        cook_recipe(choice, pantry)
        display_pantry(pantry)
