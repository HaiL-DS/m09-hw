import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self): 
        # add a book and test if it is in `book_list`.
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book("War of the Worlds", 4)
        actual = "War of the Worlds" in test_object.book_list.book_name.to_list()
        self.assertEqual(actual, True)

    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book("War of the Worlds", 4)
        test_object.add_book("War of the Worlds", 3)
        actual = len(test_object.book_list[test_object.book_list.book_name == "War of the Worlds"])
        self.assertEqual(actual, 1)
                        
    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book("War of the Worlds", 4)
        test_object.add_book("Jane Eyre", 4)
        test_object.add_book("Fight Club", 3)
        actual = test_object.has_read("War of the Worlds")
        self.assertEqual(actual, True)        
        
    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book("War of the Worlds", 4)
        test_object.add_book("Jane Eyre", 4)
        test_object.add_book("Fight Club", 3)
        actual = test_object.has_read("Harry Potter")
        message = "Test value is not false."
        self.assertFalse(actual, message) 
        
    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book("War of the Worlds", 4)
        test_object.add_book("Jane Eyre", 4)
        test_object.add_book("Fight Club", 3)
        test_object.add_book("The Divine Comedy", 5)
        test_object.add_book("The Popol Vuh", 5)
        test_object.add_book("Harry Potter", 2)
        actual = test_object.num_books_read()
        self.assertEqual(actual, 6)      

    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book("War of the Worlds", 4)
        test_object.add_book("Jane Eyre", 4)
        test_object.add_book("Fight Club", 3)
        test_object.add_book("The Divine Comedy", 5)
        test_object.add_book("The Popol Vuh", 5)
        test_object.add_book("Harry Potter", 2)
        actual_df = test_object.fav_books()
        for bookrating in actual_df.book_rating.to_list():
            self.assertEqual(bookrating>3, True)

            
if __name__ == '__main__':
    
    unittest.main(verbosity=3)