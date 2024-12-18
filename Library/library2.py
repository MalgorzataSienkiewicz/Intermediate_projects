
from books2 import(
    BooksForChildren,
    BooksForAdults,
    BookNotFoundError,
    BookNotAvailableError,
    ToManyBooks
)
from users2 import User

class Library:
    def __init__(self):
        self.books = []

    #TODO synopsis
    def list_of_books(self):

        book1 = BooksForAdults("Adults", "The Chemistry of Death", "Simon Beckett", 368,
                               True, "Synopsis", "Crime\n")
        book2 = BooksForChildren("Children", "Pucio learns to speak", "Marta Galewska-Kustra",
                                 40, True, "synopsis", "0+\n")

        self.books.append(book1)
        self.books.append(book2)
        return self.books

    def borrowed_a_book(self, title, user):
        if user.count_books() < 2:
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
        raise BookNotFoundError(f"Book '{title}' not found in the library.")



