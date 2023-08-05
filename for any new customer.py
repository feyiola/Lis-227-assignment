class LibraryManagement:
    def __init__(self):
        self.books = {}
        self.users = {}

    def add_book(self, book_id, title, author):
        self.books[book_id] = {'title': title, 'author': author, 'status': 'available'}

    def remove_book(self, book_id):
        if book_id in self.books:
            del self.books[book_id]
        else:
            print("Book not found!")

    def add_user(self, user_id, name):
        self.users[user_id] = {'name': name, 'borrowed_books': []}

    def remove_user(self, user_id):
        if user_id in self.users:
            del self.users[user_id]
        else:
            print("User not found!")

    def borrow_book(self, user_id, book_id):
        if book_id in self.books and self.books[book_id]['status'] == 'available':
            if user_id in self.users:
                self.users[user_id]['borrowed_books'].append(book_id)
                self.books[book_id]['status'] = 'borrowed'
                print("Book borrowed successfully!")
            else:
                print("User not found!")
        else:
            print("Book not available!")

    def return_book(self, user_id, book_id):
        if book_id in self.books and self.books[book_id]['status'] == 'borrowed':
            if user_id in self.users:
                if book_id in self.users[user_id]['borrowed_books']:
                    self.users[user_id]['borrowed_books'].remove(book_id)
                    self.books[book_id]['status'] = 'available'
                    print("Book returned successfully!")
                else:
                    print("Book not borrowed by this user!")
            else:
                print("User not found!")
        else:
            print("Book not borrowed or not found!")

    def display_borrowed_books(self, user_id):
        if user_id in self.users:
            borrowed_books = self.users[user_id]['borrowed_books']
            if borrowed_books:
                print("Borrowed Books:")
                for book_id in borrowed_books:
                    book = self.books[book_id]
                    print(f"Book ID: {book_id}, Title: {book['title']}, Author: {book['author']}")
            else:
                print("No books borrowed by this user.")
        else:
            print("User not found!")

    def display_inventory(self):
        print("Library Inventory - Popular Novels")
        print("{:<25} {:<25} {:<15}".format("Title", "Author", "ISBN"))
        print("="*65)
        inventory_books = [
            ("1984", "George Orwell", "978-0451524935"),
            ("To Kill a Mockingbird", "Harper Lee", "978-0061120084"),
            ("Pride and Prejudice", "Jane Austen", "978-1612930349"),
            ("The Great Gatsby", "F. Scott Fitzgerald", "978-0743273565"),
            ("Moby-Dick", "Herman Melville", "978-0142437247"),
            ("War and Peace", "Leo Tolstoy", "978-1400079988"),
            ("The Catcher in the Rye", "J.D. Salinger", "978-0316769488"),
            ("One Hundred Years of Solitude", "Gabriel García Márquez", "978-0060883287"),
            ("The Lord of the Rings", "J.R.R. Tolkien", "978-0544003415"),
            ("Brave New World", "Aldous Huxley", "978-0060850524"),
            # ... add more books here
        ]
        for book_data in inventory_books:
            title, author, isbn = book_data
            print("{:<25} {:<25} {:<15}".format(title, author, isbn))

    def display_menu(self):
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Add User")
        print("4. Remove User")
        print("5. Borrow Book")
        print("6. Return Book")
        print("7. Display Borrowed Books")
        print("8. Display Inventory")
        print("9. Exit")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")

            if choice == '1':
                book_id = input("Enter book ID: ")
                title = input("Enter book title: ")
                author = input("Enter author: ")
                self.add_book(book_id, title, author)
            elif choice == '2':
                book_id = input("Enter book ID to remove: ")
                self.remove_book(book_id)
            elif choice == '3':
                user_id = input("Enter user ID: ")
                name = input("Enter user name: ")
                self.add_user(user_id, name)
            elif choice == '4':
                user_id = input("Enter user ID to remove: ")
                self.remove_user(user_id)
            elif choice == '5':
                user_id = input("Enter user ID: ")
                book_id = input("Enter book ID to borrow: ")
                self.borrow_book(user_id, book_id)
            elif choice == '6':
                user_id = input("Enter user ID: ")
                book_id = input("Enter book ID to return: ")
                self.return_book(user_id, book_id)
            elif choice == '7':
                user_id = input("Enter user ID: ")
                self.display_borrowed_books(user_id)
            elif choice == '8':
                self.display_inventory()
            elif choice == '9':
                print("Exiting the library system.")
                break
            else:
                print("Invalid choice. Please select a valid option.")

# Create an instance of LibraryManagement
library_system = LibraryManagement()

# Run the library system
library_system.run()
