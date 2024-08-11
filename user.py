# user.py
class User:
    def __init__(self, name, user_id):
        self.__name = name
        self.__user_id = user_id
        self.__borrowed_books = []

    @property
    def name(self):
        return self.__name

    @property
    def user_id(self):
        return self.__user_id

    @property
    def borrowed_books(self):
        return self.__borrowed_books

    def borrow_book(self, book_title):
        if book_title not in self.__borrowed_books:
            self.__borrowed_books.append(book_title)

    def return_book(self, book_title):
        if book_title in self.__borrowed_books:
            self.__borrowed_books.remove(book_title)

    def __str__(self):
        return f"Name: {self.name}, User ID: {self.user_id}, Borrowed Books: {', '.join(self.borrowed_books)}"
