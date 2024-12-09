from books import BookForAdults, BookForChildren, BookNotFoundError, BookNotAvailableError
class Library:
    def __init__(self):
        self.books = []

        book1 = BookForAdults("The Chemistry of Death.", "Simon Beckett", 368,
                              True, "Synopsis", "Crime\n")
        book2 = BookForChildren("Pucio learns to speak.", "Marta Galewska-Kustra",
                                40, True, "synopsis", "0+\n")

        self.books.append(book1)
        self.books.append(book2)

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
