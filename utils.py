# utils.py
# Utility functions

# Display book inventory
def display_inventory(inventory):
    index = 0
    for row in inventory:
        print(f"{[index]} ", row)
        index += 1