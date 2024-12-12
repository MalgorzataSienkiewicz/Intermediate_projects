import sys
from books import BookNotFoundError, BookNotAvailableError
from library import Library
from users import UserNotFoundError
from initializer import Initializer


def display_library_books(library):
    library.display_books()

def display_borrowed_books(user):
    user.display_books()


def borrow_book(user, library):
    title = input("Type the title of the book you want to borrow: ")
    try:
        book = library.borrow_book(title)
        user.borrow_book(book)
    except BookNotFoundError:
        print("A book with this title was not found.")
    except BookNotAvailableError:
        print("The book with this title has been borrowed.")


def return_book(user, library):
    title = input("Type the titles of the books you want to return: ").strip()
    try:
        user.return_book(title)
        library.return_book(title)
    except BookNotFoundError:
        print("You don't have such a book.")

def login(users, name):
    for user in users:
        if user.name == name:
            return user

    raise UserNotFoundError


if __name__ == "__main__":
    library = Library()
    users = Initializer.init_users()

    user = None

    while True:
        while user is None:
            try:
                name = input("If you want to log in, type your name: ").strip()
                user = login(users, name)
                print("You are logged in!")
            except UserNotFoundError:
                print("The user doesn't exist.")

        print("1. View a list of books in your library.")
        print("2. View a list of your books. ")
        print("3. Borrow a book.")
        print("4. Return a book.")
        print("5. Log out.")
        print("6. Exit program.")

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
            return_book(user, library)
        elif option == 5:
            user = None
        elif option == 6:
            sys.exit()