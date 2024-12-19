from books2 import(
    BooksForChildren,
    BooksForAdults,
    BookNotFoundError,
    BookNotAvailableError,
    ToManyBooks
)

class Library:
    def __init__(self):
        self.books = []

        book1 = BooksForAdults("Adults", "The Chemistry of Death",
                               "Simon Beckett", 368,
                               True, "Crime\n")
        book2 = BooksForAdults("Adults", "Learning Python", "Mark Lutz",
                               1496, True, "Computer science\n")
        book3 = BooksForAdults("Adults", "Heart of the Matter", "Emily Giffin",
                               392, True, "Romance\n")
        book4 = BooksForChildren("Children", "Puss in Boots", "Roland Garrigue",
                                 24, True, "3+\n")
        book5 = BooksForChildren("Children", "The Lion Inside", "Rachel Bright",
                                 32, True, "4+\n")
        book6 = BooksForChildren("Children", "Pucio learns to speak",
                                 "Marta Galewska-Kustra",
                                 40, True, "0+\n")

        self.books.extend([book1, book2, book3, book4, book5, book6])

    def list_of_books(self):
        return self.books

    def borrowed_a_book(self, title, user):
        try:
            if user.count_books() < 2:
                for book in self.list_of_books():
                    if book.title.lower() == title and book.available:
                        book.available = False
                        user.borrow_book(book)
                        print(f"You have borrowed a book titled: '{title.capitalize()}'.\n")
                        return book
                    elif book.title.lower() == title and not book.available:
                        raise BookNotAvailableError
                raise BookNotFoundError
            raise ToManyBooks
        except BookNotAvailableError:
            print("The book is already borrowed.")
        except BookNotFoundError:
            print(f"Book '{title}' not found.")
        except ToManyBooks:
            print("You cannot borrow more than 2 books.")


    def return_a_book(self, title):
        for book in self.books:
            if book.title == title:
                book.available = True
                return
        raise BookNotFoundError(f"Book '{title}' not found in the library.")



