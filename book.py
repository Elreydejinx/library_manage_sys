# book.py
class Book:
    def __init__(self, title, author, genre, pub_date):
        self.__title = title
        self.__author = author
        self.__genre = genre
        self.__pub_date = pub_date
        self.__availability = True

    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @property
    def genre(self):
        return self.__genre

    @property
    def pub_date(self):
        return self.__pub_date

    @property
    def availability(self):
        return self.__availability

    @availability.setter
    def availability(self, status):
        self.__availability = status

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Genre: {self.genre}, Publication Date: {self.pub_date}, Available: {self.availability}"
