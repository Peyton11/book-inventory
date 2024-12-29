# main.py
# Main file for Book Inventory program

from utils import *
import csv

inventory = []

# Create CSV file if it doesn't exist
open("inventory.csv", "a")

# Add heading if file is empty
if is_empty("inventory.csv"):
    with open("inventory.csv", "w") as file:
        file.write("Title,Author,Genre,ISBN-10,ISBN-13,Page Count")

# Import current inventory from CSV file
with open("inventory.csv", "r", newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        inventory.append(row)

# Inventory operation choices
print("[1] View Inventory")
print("[2] Add Book")
print("[3] Edit Book")
print("[4] Delete Book")
operation = int(input("Enter choice: "))

# View inventory
if operation == 1:
    display_inventory(inventory)

# Append book to inventory
if operation == 2:

    # Book data
    title = str(input("Enter book title: "))
    author = str(input("Enter book author: "))
    genre = str(input("Enter book genre: "))
    isbn_10 = str(input("Enter book ISBN-10: "))
    isbn_13 = str(input("Enter book ISBN-13: "))
    page_count = int(input("Enter page count: "))

    # Add to inventory list
    new_book = [title, author, genre, isbn_10, isbn_13, page_count]
    inventory.append([new_book])

    # Write to CSV
    with open("inventory.csv", "a") as file:
        writer = csv.writer(file)
        writer.writerow(new_book)

# Edit a book from inventory
elif operation == 3:

    display_inventory(inventory)

    # Edit book attribute
    edit_index = int(input("Edit book: "))
    print("[1] Edit title")
    print("[2] Edit author")
    print("[3] Edit genre")
    print("[4] Edit ISBN-10")
    print("[5] Edit ISBN-13")
    print("[6] Edit page count")
    edit_choice = int(input("Enter choice: "))

    # Edit value
    if edit_choice == 1:
        inventory[edit_index][edit_choice - 1] = input("Enter new book title: ")
    elif edit_choice == 2:
        inventory[edit_index][edit_choice - 1] = input("Enter new book author: ")
    elif edit_choice == 3:
        inventory[edit_index][edit_choice - 1] = input("Enter new book genre: ")
    elif edit_choice == 4:
        inventory[edit_index][edit_choice - 1] = input("Enter new ISBN-10: ")
    elif edit_choice == 5:
        inventory[edit_index][edit_choice - 1] = input("Enter new ISBN-13: ")
    elif edit_choice == 6:
        inventory[edit_index][edit_choice - 1] = input("Enter new page count: ")

    # Write inventory to CSV file
    with open("inventory.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(inventory)

# Delete a book from inventory
elif operation == 4:

    display_inventory(inventory)

    # Choose book to delete
    delete_index = int(input("Delete book: "))
    inventory.pop(delete_index)

    # Display book inventory
    for rows in inventory:
        print(rows)

    # Rewrite inventory
    with open("inventory.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(inventory)
