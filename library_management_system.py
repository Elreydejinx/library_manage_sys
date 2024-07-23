from book import Book
from author import Author

from user import User


def main():
    welcome = 'Welcome to the Library Management System:'
    print(welcome)

book_list=[]
library = {}

    main_menu = input('Main Menu:\n1. Book Operations\n2. User Operations\n3. Auther Operations\n4. Quit') 
    book_op = input('Book Operations:\n1. Add a new book\n2. Borrow a book\n3. Return a book\n4. Search for a book\n5. Display all books')
    user_op = input('User Operatioins:\n1. Add a new user\n2. View user details\n3. Display all users')
    author_op = input('Author Operations:\n1. Add a new author\n2. View author details\n3. Display all authors')

    while True:
        print(main_menu) 
        choice = input('select choice')
        if choice == '1':
            book_op(library)
        elif choice == '2':
            user_op(library)
        elif choice == '3':
            author_op(library)
        elif choice == '4':
            break
def add_book(book_list):
    title = input('enter book title:')
    author = input('enter author:')
    genre = input('enter genre:')
    publication_date = input('enter publication date:')
    book = Book(title,author,genre,publication_date)
    book_list.append(book)

def view_book(book_list):
    for book in book_list:
        print(book.title)
        print(book.author)
        print(book.genre)
        print(book.publication_date)

# def book_op():
#     welcome = 'Welcome to book operations...'
#     print(welcome)

#     borrowed_books = {}
#     while True:
#         print('Book Operations:\n1. Add a new book\n2. Borrow a book\n3. Return a book\n4. Search for a book\n5. Display all books')
#         option = input('slect am options:')
#         if option == "1":
#              add_book 
#         elif option == '2':
#             borrowed_books(borrowed_books)
#         elif option == '3':
#             return_a_book = 


main()


    