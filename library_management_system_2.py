# Program for Library Management System

library = {}

def add_book():
    book_id = input("Enter Book ID:")
    book_name = input("Enter Book Name:")

    if book_id in library:
        print("Book ID already exists!")
    else:
        library[book_id] = book_name
        print("Book Added Successfully!")

def view_books():
    if library == {}:
        print("No books available")
    else:
        print("\nLibrary Books:")
        for key in library:
            print("Book ID:", key, "Book Name:", library[key])

def search_book():
    book_id = input("Enter book ID to search:")
    if book_id in library:
        print("Book Found:", library[book_id])
    else:
        print("Book Not Found")

def delete_book():
    book_id = input("Enter book ID to delete:")
    if book_id in library:
        del library[book_id]
        print("Book Deleted Successfully!")
    else:
        print("Book Not Found")

while True:
    print("\n=====LIBRARY MANAGEMENT SYSTEM=====")
    print("1.Add Book")
    print("2.View Books")
    print("3.Search Book")
    print("4.Delete Book")
    print("5.Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_book()
    elif choice == 2:
        view_books()
    elif choice == 3:
        search_book()
    elif choice == 4:
        delete_book()
    elif choice == 5:
        print("Program completed.Thank you!")
        break
    else:
        print("Invalid choice! Please try again.")
