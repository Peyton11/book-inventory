# Book Inventory Program

The **Book Inventory Program** is a simple Python-based tool to manage a collection of books. It allows users to view, add, edit, and delete book entries stored in a CSV file. This program is ideal for small-scale personal book inventory management.

## Features

- **View Inventory**: Display the list of books currently stored in the inventory.
- **Add Book**: Add a new book to the inventory with details such as title, author, genre, ISBN-10, ISBN-13, and page count.
- **Edit Book**: Modify the details of an existing book in the inventory.
- **Delete Book**: Remove a book from the inventory.

## Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/book-inventory.git
cd book-inventory
```
2. Install Python 3.x if not already installed. You can download it from python.org.

3. Run the program:
```bash
python main.py
```

## Usage

1. Run the program: After starting the program, you will see a list of operations:
```
[1] View inventory
[2] Add Book
[3] Edit Book
[4] Delete Book
Enter choice:
```

2. Choose an operation:  
    - **[1] View inventory**: Displays the list of books in the inventory.
    - **[2] Add Book**: Prompts you to enter the details of a new book.
    - **[3] Edit Books**: Allows you to select and modify an existing book's details.
    - **[4] Delete Book**: Prompts you to select and remove a book from the inventory.

3. Data Storage:
    - All data is stored in a file named `inventory.csv`.
    - If the file does not exist, it will be created automatically.
    - If the file is empty, a default header is added: `Title,Author,Genre,ISBN-10,ISBN-13,Page Count`

