# spicy_foods = [
#     {
#         "name": "Green Curry",
#         "cuisine": "Thai",
#         "heat_level": 9,
#     },
#     {
#         "name": "Buffalo Wings",
#         "cuisine": "American",
#         "heat_level": 3,
#     },
#     {
#         "name": "Mapo Tofu",
#         "cuisine": "Sichuan",
#         "heat_level": 6,
#     },
# ]

# def get_names(spicy_foods):
#     pass

# def get_spiciest_foods(spicy_foods):
#     pass

# def print_spicy_foods(spicy_foods):
#     pass

# def get_spicy_food_by_cuisine(spicy_foods, cuisine):
#     pass

# def print_spiciest_foods(spicy_foods):
#     pass

# def get_average_heat_level(spicy_foods):
#     pass

# def create_spicy_food(spicy_foods, spicy_food):
#     pass





spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]


def get_names(spicy_foods):
    """
    Return a list of strings with the names of each spicy food.
    
    Example:
        get_names(spicy_foods)
        # => ["Green Curry", "Buffalo Wings", "Mapo Tofu"]
    """
    return [food["name"] for food in spicy_foods]


def get_spiciest_foods(spicy_foods):
    """
    Return a list of dictionaries where the heat level of the food is greater than 5.
    
    Example:
        get_spiciest_foods(spicy_foods)
        # => [
        #      {"name": "Green Curry", "cuisine": "Thai", "heat_level": 9},
        #      {"name": "Mapo Tofu", "cuisine": "Sichuan", "heat_level": 6}
        #    ]
    """
    return [food for food in spicy_foods if food["heat_level"] > 5]


def print_spicy_foods(spicy_foods):
    """
    Output to the terminal each spicy food in the following format:
    "Name (Cuisine) | Heat Level: 🌶 repeated as many times as the heat_level"
    
    Example output:
        Green Curry (Thai) | Heat Level: 🌶🌶🌶🌶🌶🌶🌶🌶🌶
        Buffalo Wings (American) | Heat Level: 🌶🌶🌶
        Mapo Tofu (Sichuan) | Heat Level: 🌶🌶🌶🌶🌶🌶
    """
    for food in spicy_foods:
        heat_emojis = "🌶" * food["heat_level"]
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_emojis}")


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    """
    Return a single dictionary for the spicy food whose cuisine matches the cuisine being passed.
    
    Example:
        get_spicy_food_by_cuisine(spicy_foods, "American")
        # => {"name": "Buffalo Wings", "cuisine": "American", "heat_level": 3}
    """
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
    return None  # In case no food matches the given cuisine


def print_spiciest_foods(spicy_foods):
    """
    Output to the terminal only the spicy foods that have a heat level greater than 5,
    using the same format as print_spicy_foods().
    
    Example output:
        Green Curry (Thai) | Heat Level: 🌶🌶🌶🌶🌶🌶🌶🌶🌶
        Mapo Tofu (Sichuan) | Heat Level: 🌶🌶🌶🌶🌶🌶
    """
    # Filter for foods with heat_level greater than 5 and print them
    for food in spicy_foods:
        if food["heat_level"] > 5:
            heat_emojis = "🌶" * food["heat_level"]
            print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_emojis}")


def get_average_heat_level(spicy_foods):
    """
    Return an integer representing the average heat level of all the spicy foods.
    
    Example:
        get_average_heat_level(spicy_foods)
        # => 6
    """
    total_heat = sum(food["heat_level"] for food in spicy_foods)
    return total_heat // len(spicy_foods) if spicy_foods else 0


def create_spicy_food(spicy_foods, spicy_food):
    """
    Add a new spicy food dictionary to the list and return the updated list.
    
    Example:
        create_spicy_food(
            spicy_foods,
            {
                'name': 'Griot',
                'cuisine': 'Haitian',
                'heat_level': 10,
            }
        )
    """
    spicy_foods.append(spicy_food)
    return spicy_foods
