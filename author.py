class Author:

    def __init__(self, author, biograrphy):
        self.author = author
        self.biography = biograrphy
        

    def author_info(self):
        print(f'Author: {self.author}')
        print(f'Biography: {self.biography}')

    def get_author_info(self):
        return self.author
   
    def set_author_info(self,author):
        self.author = input('enter authors name:')
        print(author)

    def get_biography(self):
        return self.biography
    
    def set_biography(self,biography):
        self.biography = input(f'enter biography name:')
        print(biography)


author_info = input('enter author:')
biography = input('enter biography:')
print(author_info)
print(biography)