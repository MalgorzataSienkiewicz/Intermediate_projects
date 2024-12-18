import users2
from books2 import (
    BooksForChildren,
    BooksForAdults,
    BookNotFoundError,
    BookNotAvailableError,
    ToManyBooks
)
from users2 import User

class Library:
    books = []

    #TODO synopsis
    def list_of_books(self):

        book1 = BooksForAdults("The Chemistry of Death.", "Simon Beckett", 368,
                               True, "Synopsis", "Crime\n")
        book2 = BooksForChildren("Pucio learns to speak.", "Marta Galewska-Kustra",
                                 40, True, "synopsis", "0+\n")

        Library.books.append(book1)
        Library.books.append(book2)
        return Library.books

    def borrowed_a_book(self, title, books, user):
        if User.count_books(user.books) < 2:
            for book in self.list_of_books():
                if book.title == title and book.available:
                    book.available = False
                    user.borrow_book(book)
                    return book
                elif book.title == title and not book.available:
                    raise BookNotAvailableError("The book is already borrowed.")
            raise BookNotFoundError(f"Book '{title}' not found.")
        raise ToManyBooks("You cannot borrow more than 2 books.")

    def return_a_book(self, title):
        for book in self.books:
            if book.title == title:
                book.available = True
                return
        raise BookNotFoundError(f"Book 'title' not found in the library.")



