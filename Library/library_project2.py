import sys
from books2 import(
    Books,
    BookNotAvailableError,
    BookNotFoundError,
    ToManyBooks
)
from library2 import Library
from users2 import User, UserNotFoundError

def display_library_books(library):
    for book in library.list_of_books():
        book.display_info_book()

def display_borrowed_books(user):
    user.display_books()

def borrow_book(user, library):
    title = input("Type the title of the book you want to borrow: ")
    try:
        library.borrowed_a_book(title, user)
        print(f"You have borrowed a book titled: '{title}'.\n")
    except BookNotFoundError:
        print("A book with this title was not found.")
    except BookNotAvailableError:
        print("The book with this title has been borrowed.")

def return_book(user, library):
    title = input("Type the title of the book you want to return: ").strip()
    try:
        user.return_book(title)
        library.return_a_book(title)
        print(f'Book "{title}" successfully returned.\n')
    except BookNotFoundError:
        print("A book with this title was not found.")

def login(users, name):
    for user in users:
        if user.name == name:
            return user
    raise UserNotFoundError(f"The user doesn't exist.")

if __name__ == "__main__":
    library = Library()
    users = User.users_names()
    books = Books

    user = None

    while True:
        while user is None:
            try:
                name = input("If you want to log in type your name, "
                             "if not type 'exit': ").strip().lower()
                if not name == 'exit':
                    user = login(users, name)
                    print(f"{name} you are logged in!\n")
                else:
                    sys.exit()
            except UserNotFoundError:
                print("The user doesn't exist.")

        print("1. View a list of books in your library.")
        print("2. View a list of your books. ")
        print("3. Borrow a book.")
        print("4. Return a book.")
        print("5. Log out.")
        print("6. Exit program.")

        try:
            option = int(input("Type option(1, 2, 3, 4, 5 or 6): \n"))
            if option not in [1, 2, 3, 4, 5, 6]:
                raise ValueError
        except ValueError:
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


