# main.py
import re
from book import Book
from user import User
from author import Author

books = []
users = []
authors = []

def display_main_menu():
    print("Welcome to the Library Management System!")
    print("Main Menu:")
    print("1. Book Operations")
    print("2. User Operations")
    print("3. Author Operations")
    print("4. Quit")

def display_book_menu():
    print("Book Operations:")
    print("1. Add a new book")
    print("2. Borrow a book")
    print("3. Return a book")
    print("4. Search for a book")
    print("5. Display all books")

def display_user_menu():
    print("User Operations:")
    print("1. Add a new user")
    print("2. View user details")
    print("3. Display all users")

def display_author_menu():
    print("Author Operations:")
    print("1. Add a new author")
    print("2. View author details")
    print("3. Display all authors")

def add_book():
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    genre = input("Enter book genre: ")
    pub_date = input("Enter publication date (YYYY-MM-DD): ")
    books.append(Book(title, author, genre, pub_date))
    print("Book added successfully!")

def borrow_book():
    title = input("Enter book title to borrow: ")
    for book in books:
        if book.title == title:
            if book.availability:
                user_id = input("Enter your user ID: ")
                for user in users:
                    if user.user_id == user_id:
                        user.borrow_book(title)
                        book.availability = False
                        print("Book borrowed successfully!")
                        return
                print("User ID not found.")
                return
            else:
                print("Book is not available.")
                return
    print("Book not found.")

def return_book():
    title = input("Enter book title to return: ")
    for book in books:
        if book.title == title:
            user_id = input("Enter your user ID: ")
            for user in users:
                if user.user_id == user_id:
                    user.return_book(title)
                    book.availability = True
                    print("Book returned successfully!")
                    return
            print("User ID not found.")
            return
    print("Book not found.")

def search_book():
    title = input("Enter book title to search: ")
    for book in books:
        if book.title == title:
            print(book)
            return
    print("Book not found.")

def display_books():
    if books:
        for book in books:
            print(book)
    else:
        print("No books available.")

def add_user():
    name = input("Enter user name: ")
    user_id = input("Enter user ID: ")
    users.append(User(name, user_id))
    print("User added successfully!")

def view_user_details():
    user_id = input("Enter user ID to view details: ")
    for user in users:
        if user.user_id == user_id:
            print(user)
            return
    print("User not found.")

def display_users():
    if users:
        for user in users:
            print(user)
    else:
        print("No users available.")

def add_author():
    name = input("Enter author name: ")
    biography = input("Enter author biography: ")
    authors.append(Author(name, biography))
    print("Author added successfully!")

def view_author_details():
    name = input("Enter author name to view details: ")
    for author in authors:
        if author.name == name:
            print(author)
            return
    print("Author not found.")

def display_authors():
    if authors:
        for author in authors:
            print(author)
    else:
        print("No authors available.")

def main():
    while True:
        display_main_menu()
        choice = input("Select an option (1-4): ")
        if choice == '1':
            while True:
                display_book_menu()
                book_choice = input("Select an option (1-5): ")
                if book_choice == '1':
                    add_book()
                elif book_choice == '2':
                    borrow_book()
                elif book_choice == '3':
                    return_book()
                elif book_choice == '4':
                    search_book()
                elif book_choice == '5':
                    display_books()
                else:
                    print("Invalid choice.")
                cont = input("Continue with Book Operations? (y/n): ")
                if cont.lower() != 'y':
                    break
        elif choice == '2':
            while True:
                display_user_menu()
                user_choice = input("Select an option (1-3): ")
                if user_choice == '1':
                    add_user()
                elif user_choice == '2':
                    view_user_details()
                elif user_choice == '3':
                    display_users()
                else:
                    print("Invalid choice.")
                cont = input("Continue with User Operations? (y/n): ")
                if cont.lower() != 'y':
                    break
        elif choice == '3':
            while True:
                display_author_menu()
                author_choice = input("Select an option (1-3): ")
                if author_choice == '1':
                    add_author()
                elif author_choice == '2':
                    view_author_details()
                elif author_choice == '3':
                    display_authors()
                else:
                    print("Invalid choice.")
                cont = input("Continue with Author Operations? (y/n): ")
                if cont.lower() != 'y':
                    break
        elif choice == '4':
            print("Quitting the application. Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
