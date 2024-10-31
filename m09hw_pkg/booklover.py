import numpy as np
import pandas as pd

class BookLover:
    
    def __init__(self, name, email, fav_genre):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        #self.num_books = 0
        self.book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})
        
    def add_book(self, book_name, book_rating):
        if book_name in self.book_list.book_name.to_list():  
            print(f"You've read the book '{book_name}' already!")
        else:
            new_book = pd.DataFrame({
                                    'book_name': [book_name], 
                                    'book_rating': [int(book_rating)]
                                   })

            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
            
    def has_read(self, book_name):
        if book_name in self.book_list.book_name.to_list():
            return True
        return False

    def num_books_read(self):
        return self.book_list.shape[0]
    
    def fav_books(self):
        return self.book_list[self.book_list.book_rating > 3]

    
if __name__ == '__main__':
    
    test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
    test_object.add_book("War of the Worlds", 4)
    test_object.add_book("Jane Eyre", 4)
    test_object.add_book("Fight Club", 3)
    test_object.add_book("The Divine Comedy", 5)
    test_object.add_book("The Popol Vuh", 5)
    test_object.add_book("Harry Potter", 2)
    test_object.add_book("Harry Potter", 3)
    print(test_object.has_read("Jane Eyre"))
    print(test_object.has_read("Wuthering Heights"))
    print(test_object.num_books_read())
    print(test_object.fav_books())
    
    
   