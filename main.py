from library import Library

def main():
    library = Library()

    while True:
        print("\n~~~~~~~ LIBRARY MENU ~~~~~~~~")
        print("1. Add Book")
        print("2. List Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Book Title: ")
            author = input("Author: ")
            isbn = input("ISBN: ")
            library.add_book(title, author, isbn)

        elif choice == "2":
            library.list_books()

        elif choice == "3":
            isbn = input("Enter ISBN to borrow: ")
            library.lend_book(isbn)

        elif choice == "4":
            isbn = input("Enter ISBN to return: ")
            library.return_book(isbn)

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid option! Try again!")

if __name__ == "__main__":
    main()

