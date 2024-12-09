import sys
from books import BookForAdults, BookForChildren
from library import Library
from users import User

def display_library_books(library):
    for book in library.books:
        book.display_book_info()

def display_borrowed_books(user):
    for book in user.books:
        book.display_book_info()


def borrow_book(user, library):
    title = input("Type the title of the book you want to borrow: ")
    book = library.borrow_book(title)
    user.borrow_book(book)

def return_book():
    pass


if __name__ == "__main__":
    library = Library()
    user = User("Gosia")

    while True:
        print("1. View a list of books in your library.")
        print("2. View a list of your books. ")
        print("3. Borrow a book.")
        print("4. Return a book.")
        print("5. Exit program.")

        try:
            option = int(input("Type option(1, 2, 3, 4 or 5): \n"))
            if option not in [1, 2, 3, 4, 5]:
                raise Exception
        except Exception:
            print("Incorrect command. Try again.\n")


        if option == 1:
            display_library_books(library)
        elif option == 2:
            display_borrowed_books(user)
        elif option == 3:
            borrow_book(user, library)
        elif option == 4:
            return_book()
        elif option == 5:
            sys.exit()