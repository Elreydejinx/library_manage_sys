class User: 

    self = {}
    
    def __init__ (self,name, library_ID):
        self.name = name
        self.library_ID = library_ID
        self.borrowed_books = []

    def nAme(self):
        fstnme = input('enter your first name:')
        mddlenme = input('enter your middle name:')
        lstnme = input('enter your last name:')
        fulname = (f'{fstnme} {mddlenme} {lstnme}')
        print(f'your name is: {fulname} welcome to our library!!!')

    def get_nAme(self):
        return self.nAme
    
    def set_nAme(self,name):
        self.nAme= name


 # library_id 
    def Library_ID(self):   
        id_num = input('Enter your ID_num?:')
        user_name = input('Enter your User Name:')
        password = input('Enter your password:') 
        LB_id = (f'{id_num}{user_name}')
        print(f'{LB_id} your password is {password} dont show it to others!')

    def get_Library_ID(self):
        return self.Library_ID
    
    def set_Library_ID(self, library_ID):
        self.Library_ID = library_ID

 #borrowed_book_titles

    def books_borrowed(self):
        user_name = input('enter username:')
        user_num = input('enter user number:')
        num_of_books = int(input('how many books does this user have:'))
        title_of_book = input('enter book title or titles user has borrowed:')
        library_id = (f'{user_name}{user_num}')
        books_borrowed = (f'{library_id} has borrowed \n {num_of_books} books:\n {title_of_book}')
        print(books_borrowed)

    def get_books_borrowed(self):
        return self.books_borrowed
    
    def set_books_borrowed(self, books_borrowed):
        self.books_borrowed = books_borrowed
# user info

    def user_info(self):
        user_name = input('enter your user name:')
        library_num = input('enter your library number:')
        books_checked_out = input('number of books checked out:')
        user_info = ( f'{library_num}{user_name} has {books_checked_out} books checked out....')
        print(user_info)

    def get_user_info(self):
        return self.user_info
    
    def set_user_info(self, user_info):
        self.user_info = user_info


nAme = input('enter your full name:')
Library_ID = input('enter your user number followed by your username:')
books_borrowed = input('enter the amount and title of books borrowed')
user_info = (f'{nAme}\n{Library_ID}\n{books_borrowed}')
print(user_info)