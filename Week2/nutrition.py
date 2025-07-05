data = {
    'apple': 95,
    'banana': 105,
    'orange': 62,
    'grape': 62,         # per cup
    'strawberry': 49,    # per cup, halves
    'watermelon': 46,    # per cup, diced
    'pineapple': 82,     # per cup, chunks
    'blueberry': 84,     # per cup
    'lemon': 17,
    'lime': 20,
    'peach': 59,
    'pear': 102,
    'cherry': 77,        # per cup, with pits
    'plum': 30,
    'kiwi': 42,
    'mango': 99,
    'cantaloupe': 53,    # per cup, diced
    'avocado': 234,      # per whole fruit, Hass
    'grapefruit': 52,    # per half, medium
    'raspberry': 64      # per cup
}

item = input("Item: ").casefold()

if item in data:
    print(f"Calories: {data[item]}")

