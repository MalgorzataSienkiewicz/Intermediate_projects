from books import BookNotFoundError, BookNotAvailableError
from initializer import Initializer
class Library:
    def __init__(self):
        self.books = Initializer.init_books()

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title and book.available:
                book.available = False
                return book
            elif book.title == title and not book.available:
                raise BookNotAvailableError
        raise BookNotFoundError


    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                book.available = True
                return

    def display_books(self):
        for book in self.books:
            book.display_book_info()
