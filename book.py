class Book:

    def __init__(self, title, author, genre, publication_date):
        self.title = title
        self.author = author
        self. genre = genre
        self.publication_date = publication_date
        self.is_available = True

          

    def add_a_book(self):
        title = input('enter title:')
        author = input('enter author:')
        genre = input('enter genre:')
        publication_date = input('enter publication date:')
        book_added= {title,
                       author,
                       genre,
                       publication_date}
        print(f'this book: \n{book_added} wad added ')
    
    def get_add_a_book(self):
        return self.author

    def set_add_a_book(self, author):
        self.author = add_a_book
        print(author)


    def borrowed_books(self):
        book_title = input('enter desired title:')
        book_author = input('enter authors name:')
        book_genre = input('enter genre:')
        book_publication_date =input('enter publication date:')
        borrowed_book = {book_title, 
                         book_author,
                         book_genre,
                         book_publication_date}
        print(f'{borrowed_book} was borrowed')
    
    def get_borrowed_books(self):
        return self.title
    
    def set_borrowed_books(self,title):
        self.title = borrowed_books
        print(title)
    
    
add_a_book = input('enter title:'),input('enter author:'),input('enter genre:'),input('enter publication date:') 
print(add_a_book)

borrowed_books = input('enter borrowed book:'), input('enter author:'), input('enter genre:'), input('enter publication date:')
print(borrowed_books)
