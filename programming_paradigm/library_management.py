
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.__is_checked_out = False

    # the book is out. A user has it
    def check_out(self):
        self.__is_checked_out = True

    # the library has the book. No user has it
    def check_in(self):
        self.__is_checked_out = False

class Library():
    def __init__(self):
        self.__books = []

    def add_book(self, title, author):
        # create a new book object
        new_book = Book(title, author)

        # add it to the list
        self.__books.append(new_book)

    def check_out_book(self, title):
        # find the book in the list
        for book in self.__books:
            # once it's found
            if book.title == title:
                # check out (make it unavailable)
                book.check_out()
            else:
                return False
    

    def return_book(self):
        # find the book in the list
        for book in self.__books: 
            # once it's found
            if book.title == title:
                # check in (make it available)
                book.check_in()
            else:
                return False
        

    def list_available_books(self):
        for book in self.__books:
            print(book)
    