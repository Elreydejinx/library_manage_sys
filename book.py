import datetime
class Book:

    def __init__(self, title, author, genre, publication_date,):
        self.title = title
        self.author = author
        self. genre = genre
        self.publication_date = publication_date
        self.is_available = True

    def add_a_book(self):
        title = input('enter title:')
        author = input('enter author:')
        genre = input('enter genre:')
        publication_date = input('when was this book published?')
        
        book_info = (title,author,genre,publication_date)
        for i in book_info:
            print(i)

    def borrow_a_book(self):
        title = input('enter title')
        date_borrowed = input('what is todays date')
        how_many_books_borrowed = input('how many books do you alreday have?')
        for i in input:
            if input >= 5:
                print('you have the max # of books allowed')
            elif input <= 5:
                print('you are close to your max amount but what would you like to borrow:')
            elif input >= 0:
                print('you can get 5 books max what would you like to borrow')
            else:
                print('not a valid entry try again')
        is_available = input('is this book available: yes/no')
        for i in is_available:
            if input == 'yes':
                print('this book is available for check out')
            else:
                print('this book is not available for checkout')
        borrow_a_book = (title, date_borrowed, how_many_books_borrowed, is_available)
        for i in borrow_a_book:
            print(i)


    def return_book(self):
        book_title = input('what book are you returning:')
        return_date = input('enter todays date:')
        user = input('enter your library_ID info:')
        return_book = (f'{user} has returned {book_title}\n{return_date}')
        for i in return_book:
            print(i)

    def search_for_a_book(self):
        browse_books = input('what book are you looking for?')
        for input in browse_books:
            if input == title


            
Book(title= input(), author= input(), genre= input(), publication_date= input())