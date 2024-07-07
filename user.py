class User:
 
 # name - first middle last
    first = input('please enter your first name:')
    middle = input('please enter your middle name:')
    last = input('please enter your last name:')
    name = (f'welcome:{first} {middle} {last}!!!')
 
 
 # library_id 
    id_num = input('Enter your ID_num?:')
    user_name = input('Enter your User Name:')
    password = input('Enter your password:')

    library_ID = (f'{id_num}{user_name}')
 #borrowed_book_titles
    num_of_books = int(input('how many books does this user have:'))
    title_of_book = input('enter book title or titles user has borrowed:')
    borrowed_books = (f'''{library_ID} has borrowed {num_of_books} books:
                                  {title_of_book}''')
# user info
    user_info = [name,borrowed_books]
    for i in user_info:
        print(i)
