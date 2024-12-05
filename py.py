dictionaries = [
    {"Puppies": 17, 'Kittens': 9, "Birds": 23, 'Fish': 90, "Hamsters": 49},
    {"Puppies": 23, "Birds": 29, "Fish": 20, "Mice": 20, "Snakes": 7},
    {"Fish": 203, "Hamsters": 93, "Snakes": 25, "Kittens": 89},
    {"Birds": 20, "Puppies": 90, "Snakes": 21, "Fish": 10, "Kittens": 67}
]

total = 0

for diction in dictionaries:
    try:
        total += diction['Puppies']  # Try to access the 'Puppies' key
    except KeyError:
        diction['Puppies'] = 0  # If the key is missing, initialize it to 0 and continue
        total += diction['Puppies']

print("Total number of puppies:", total)