# utils.py
# Utility functions

# Display book inventory
def display_inventory(inventory):
    index = 0
    for row in inventory:
        print(f"{[index]} ", row)
        index += 1

# Check if file is empty
def is_empty(file):
    with open("inventory.csv", "r") as file:
        first_character = file.read(1)
        if not first_character:
            return True
        else:
            return False