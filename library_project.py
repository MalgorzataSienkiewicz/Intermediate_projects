import sys
from books import BookForAdults, BookForChildren , BookNotFoundError, BookNotAvailableError
from library import Library
from users import User, UserNotFoundError


def display_library_books(library):
    for book in library.books:
        book.display_book_info()

def display_borrowed_books(user):
    for book in user.books:
        book.display_book_info()


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
    title = input("Type the titles of the books you want to return: ").lower().strip()
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
    user1 = User("Gosia")
    user2 = User("Tomek")
    user3 = User("Radoslaw")
    user4 = User("Artur")
    user5 = User("Piotr")

    users = [user1, user2, user3, user4, user5]

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